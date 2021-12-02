#
# 21fa-cs115bc
#
# lab13.py
#
# A.Nicolosi
# 20211201
#
# Practice with classes.

# TODO: Write a bare-bone class InvalidDateError that inherits from ValueError
# Your constructor should allow for up to three argument (for the month,
# day, and year).  Hint: recall the syntax for default parameter values.

class InvalidDateError(ValueError):
    
    def __init__(self, m, d, y):
        if m > 12:
            message = "Invalid Month"
        elif d > Date.daysInMonth[m]:
            message = "Invalid Day"
        super(InvalidDateError, self).__init__(message)



# Fill in the missing part in the class Date below
class Date:
    '''
    Date abstraction

    Demonstrate getter/setter methods and operator overloading
    '''

    daysInMonth = [31,          # not really using index 0 (dec of prev year)
                   31, 28, 31,  # jan, (non-leap) feb, mar
                   30, 31, 30,  # apr, may, jun
                   31, 31, 30,  # jul, aug, sep
                   31, 30, 31]  # oct, nov, dec

    def isLeapYear(year):
        '''
        Check if year is a leap year
        '''
        # Every fourth year is a leap year,
        # except that every one-hundreth year it isn't,
        # but every four-hundreth year is a leap year after all!
        return True if (year%4==0 and year%100!=0) or year%400==0 else False

    def _validateCheckFeb29(m, d, y):
        return 2 == m and 29 == d and Date.isLeapYear(y)

    def validate_params(m, d, y):
        # Return True if m, d, y represent a valid date
        # Start by checking if that's a valid Feb 29 (see
        # helper above); then check if d is a valid day
        # in month m
        try:
            return True if (1<=d<=Date.daysInMonth[m] and 1<=m<=12) or Date._validateCheckFeb29(m,d,y) else False
        except IndexError:
            return False
    
    def __init__(self, month=1, day=1, year=1970):
        # Call self.validate to ensure that the parameters
        # make a valid date.  Raise an InvalidDateError if not.
        # If all is good, initialize the attributes _month, _day, and
        # _year
        if Date.validate_params(month, day, year):
            self._month = month
            self._day = day
            self._year = abs(year)
            self.ce = True if year >= 0 else False # Negative years are interpreted as the year BCE
        else:
            raise InvalidDateError(month, day, year)

    def __repr__(self):
        # Make sure to return a string that looks like a valid
        # call to the class constructor
        # Ex: Date(12, 31, 2021)
        return f"Date({self.get_month()}, {self.get_day()}, {self.get_year()})"

    def __str__(self):
        # Return a string in the format mm/dd/yyyy
        return f"{self._month:02}/{self.get_day():02}/{self.get_year():04}"

    # Write getters and setters
    # NB: Setter should check that the resulting date is valid
    # *before* affecting the change
    
    def get_month(self):
        return self._month

    def get_day(self):
        return self._day

    def get_year(self):
        return self._year

    def set_month(self, month):
        self._month = month if Date.validate_params(month, self.get_day(), self.get_year()) else self.get_month()

    def set_day(self, day):
        self._day = day if Date.validate_params(self.get_month(), day, self.get_year()) else self.get_day()

    def set_year(self, year):
        self._year = abs(year) if Date.validate_params(self.get_month(), self.get_day(), year) else self.get_year()
        self.ce = True if year >= 0 else False
        
    # Date arithmetic!

    def __eq__(self, other):
        if type(other) != Date:
            raise TypeError("other has to be a valid date as well.")
        if self.get_day() == other.get_day() \
            and self.get_month() ==  other.get_month()\
            and self.get_year() == other.get_year()\
            and self.ce == other.ce:
            return True
        else:
            return False

    def __ne__(self, other):
        if type(other) != Date:
            raise TypeError("Cannot compare date to non-date")
        return not(self == other)

    def __lt__(self, other):
        if type(other) != Date:
            raise TypeError("Cannot compare date to non-date")
        if self.get_year() < other.get_year():
            return True
        elif self.get_month() < other.get_month() and self.get_year() == other.get_year():
            return True
        elif self.get_day() < other.get_day() and self.get_month() == other.get_month() and self.get_year() == other.get_year():
            return True
        return False

    def __ge__(self, other):
        return not (self < other)

    def __le__(self, other):
        return self<other or self==other

    def __gt__(self, other):
        return not self<=other

    def __add__(self, deltaInDays):
        '''Computes the date following `self` by the specified number of days'''
        out = self
        dim = Date.daysInMonth
        if Date.isLeapYear(out.get_year()):
            dim[2] = 29
        while deltaInDays > 0:
            if dim[out.get_month()] < out.get_day() + deltaInDays:
                if out.get_day() + deltaInDays > sum(dim)-31:
                    deltaInDays -= sum(dim)-31
                    out.set_year(out.get_year()+1)
                elif out.get_month() < 12:
                    deltaInDays -= dim[out.get_month()]-out.get_day()+1
                    out.set_day(1)
                    out.set_month(out.get_month()+1)
                else:
                    deltaInDays -= dim[out.get_month()]-out.get_day()+1
                    out.set_day(1)
                    out.set_month(1)
                    out.set_year(out.get_year()+1)
            else:
                out.set_day(out.get_day()+deltaInDays)
                deltaInDays = 0
        return out