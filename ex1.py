class Date:
    def __init__(self, dd_mm_yy):
        self.dd_mm_yy = str(dd_mm_yy)

    @classmethod
    def formation(cls, dd_mm_yy):
        try:
            formated_date = list(map(int, str(dd_mm_yy).split("-")))
            return formated_date
        except ValueError:
            return print('Please write the date in "dd-mm-yy" format using numbers')

    @staticmethod
    def check(dd_mm_yy):
        check_list = list(map(int, str(dd_mm_yy).split("-")))
        if check_list[0] > 31:
            print("Number of days shouldn't exceed 31")
        else:
            if check_list[1] > 12:
                print("Number of months shouldn't exceed 12")
            else:
                print("Everything is fine")

wedding = Date('11-05-21')
print(wedding.dd_mm_yy)
print(wedding.formation('11-text-21'))
print(wedding.check('11-05-21'))



