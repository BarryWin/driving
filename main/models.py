from django.db import models

class Tranport(models.Model):
    title = models.CharField('Навзание', max_length=60)
    categ = models.CharField('Категория', max_length=5)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/avtoschool/{self.id}'

    class Meta:
        verbose_name = 'Справочник транспорта'
        verbose_name_plural = 'Справочник трансопрта'

class DrivingCard(models.Model):
    date = models.DateTimeField('Дата занятия')
    comment = models.CharField('Комментарий инструктора', max_length=250)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/avtoschool/{self.id}'

    class Meta:
        verbose_name = 'Карточка вождения'
        verbose_name_plural = 'Карточки вождения'

class Ucheniki(models.Model):
    name = models.CharField('Имя', max_length=250)
    fam = models.CharField('Фамилия', max_length=250)
    otch = models.CharField('Отчество', max_length=250, null=True)
    fio = models.CharField('ФИО', max_length=60)
    address = models.CharField('Адрес проживания', max_length=250)
    tel = models.CharField('Телефон', max_length=20)
    email = models.CharField('Телефон', max_length=150)
    photo = models.CharField('Фотография', max_length=150)
    gruppa = models.CharField('Группа', max_length=10)
    date_rogd = models.DateField('Дата рождения')
    nomdog = models.CharField('Номер договора', max_length=60)
    nomspravki = models.CharField('Номер медицинской справки', max_length=60)

    def __str__(self):
        return self.fio

    def get_absolute_url(self):
        return f'/avtoschool/{self.id}'

    class Meta:
        verbose_name = 'Ученики'
        verbose_name_plural = 'Ученики'

class Sotrudniki(models.Model):
    name = models.CharField('Имя', max_length=250)
    fam = models.CharField('Фамилия', max_length=250)
    otch = models.CharField('Отчество', max_length=250, null=True)
    fio = models.CharField('ФИО', max_length=250)
    tel = models.CharField('Телефон', max_length=20)
    email = models.CharField('Телефон', max_length=150)
    photo = models.CharField('Фотография', max_length=150)
    date_rogd = models.DateField('Дата рождения')
    dolgn = models.CharField('Должность', max_length=60)
    ucheniki = models.TextField('Ученики', max_length=500)

    def __str__(self):
        return self.fio

    def get_absolute_url(self):
        return f'/avtoschool/{self.id}'

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

class Trvperiod(models.Model):
    gosnomer = models.CharField('Гос.Номер', max_length=60)
    nazvavto = models.CharField('Макрка, модель', max_length=20)
    tip_transm = models.CharField('Тип трансмиссии', max_length=20)
    prog_obuch = models.CharField('Программа обучения', max_length=60)
    fio = models.ForeignKey(Sotrudniki, on_delete=models.CASCADE)

    def __str__(self):
        return self.gosnomer

    def get_absolute_url(self):
        return f'/avtoschool/{self.id}'

    class Meta:
        verbose_name = 'Транспорт в период обучения'
        verbose_name_plural = 'Транспорт в период обучения'

class Progobuch(models.Model):
    categ = models.CharField('Категория', max_length=10)
    comment = models.TextField('Комментарий')
    temi = models.TextField('Темы')
    chasi = models.CharField('Часы', max_length=2)

    def __str__(self):
        return self.categ

    def get_absolute_url(self):
        return f'/avtoschool/{self.id}'

    class Meta:
        verbose_name = 'Программа обучения'
        verbose_name_plural = 'Программа обучения'

class Group(models.Model):
    nazv = models.CharField('Номер группы', max_length=20)
    categ = models.CharField('Категория', max_length=20)
    fio = models.TextField('ФИО')
    nach_obuch = models.DateField('Начало обучения')
    konec_obuch = models.DateField('Конец обучения')

    def __str__(self):
        return self.nazv

    def get_absolute_url(self):
        return f'/avtoschool/{self.id}'

    class Meta:
        verbose_name = 'Список групп'
        verbose_name_plural = 'Список групп'

class Rasp_teor(models.Model):
    date_zan = models.DateTimeField('Дата занятия')
    nazv = models.ForeignKey(Group, on_delete=models.CASCADE)
    fio = models.ForeignKey(Sotrudniki, on_delete=models.CASCADE)
    status = models.CharField('Статус', max_length=20)

    def __str__(self):
        return self.status

    def get_absolute_url(self):
        return f'/avtoschool/{self.id}'

    class Meta:
        verbose_name = 'Расписание теоретических занятий'
        verbose_name_plural = 'Расписание теоретических занятий'

class Otchet(models.Model):
    nomgrup = models.CharField('Номер группы', max_length=20)
    datenach = models.DateField('Дата начала обучения', max_length=20)
    kolvo = models.CharField('Количество челвоек', max_length=20)
    kolvozdav = models.CharField('Количесвто сдавших экзамен', max_length=20)
    sotrud = models.CharField('Сотрудники', max_length=20)


    def __str__(self):
        return self.nomgrup

    def get_absolute_url(self):
        return f'/avtoschool/{self.id}'

    class Meta:
        verbose_name = 'Отчет'
        verbose_name_plural = 'Отчет'

class Ulici(models.Model):
    naimulici = models.CharField('Наименование улицы', max_length=100)

    def __str__(self):
        return self.naimulici

    def get_absolute_url(self):
        return f'/avtoschool/{self.id}'

    class Meta:
        verbose_name = 'Улицы'
        verbose_name_plural = 'Улицы'

class Naspunct(models.Model):
    naimnaspunct = models.CharField('Наименование населенного пункта', max_length=100)

    def __str__(self):
        return self.naimnaspunct

    def get_absolute_url(self):
        return f'/avtoschool/{self.id}'

    class Meta:
        verbose_name = 'Населенный пункт'
        verbose_name_plural = 'Населенные пункты'

class Danuch(models.Model):
    famdanuch = models.CharField('Фамилия', max_length=100)
    namedanuch = models.CharField('Имя', max_length=100)
    otchdanuch = models.CharField('Отчетсво', max_length=100, blank=True)
    daterogddanuch = models.DateField()
    naspunkt = models.ForeignKey(Naspunct, on_delete=models.PROTECT)
    ulica = models.ForeignKey(Ulici, on_delete=models.PROTECT)
    nomdoma = models.CharField('Номер дома', max_length=100)
    nomkvart = models.CharField('Номер квартиры', max_length=100)

    def __str__(self):
        return [self.famdanuch, self.namedanuch, self.otchdanuch]


    def get_absolute_url(self):
        return f'/avtoschool/{self.id}'

    class Meta:
        verbose_name = 'фио индивида'
        verbose_name_plural = 'фио индивида'

class Dogovor(models.Model):
    nomerdog = models.CharField('Номер договора', max_length=20)
    datesost = models.DateField()
    stoimostobuch = models.PositiveIntegerField('Стоимость обучения')

    categ = models.ForeignKey(Progobuch, on_delete=models.PROTECT)

    uchenik = models.ForeignKey(Danuch, on_delete=models.PROTECT)

    daterastor = models.DateField()
    prichrast = models.CharField('Причина расторжения', max_length=100, blank=True)
    datepolnop = models.DateField()
    datenach = models.DateField(default=None)
    dateokonch = models.DateField(default=None)

    def __str__(self):
        return self.nomerdog

    def get_absolute_url(self):
        return f'/avtoschool/{self.id}'

    class Meta:
        verbose_name = 'Договор'
        verbose_name_plural = 'Договор'

class Zurnal(models.Model):
    fiouch = models.CharField('фио', max_length=100)

    def __str__(self):
        return self.fiouch

    def get_absolute_url(self):
        return f'/avtoschool/{self.id}'

    class Meta:
        verbose_name = 'Журнал'
        verbose_name_plural = 'Журнал'

class Documenti(models.Model):
    viddoc = models.CharField('фио', max_length=100)
    datedoc = models.CharField('фио', max_length=100)
    nomerdoc = models.CharField('фио', max_length=100)
    seriadoc = models.CharField('фио', max_length=100)
    kemvidan = models.CharField('фио', max_length=100)
    opisandoc = models.CharField('фио', max_length=100)
    fiouch = models.CharField('фио', max_length=100)
    fiouch = models.CharField('фио', max_length=100)
    fiouch = models.CharField('фио', max_length=100)

    def __str__(self):
        return self.fiouch

    def get_absolute_url(self):
        return f'/avtoschool/{self.id}'

    class Meta:
        verbose_name = 'Журнал'
        verbose_name_plural = 'Журнал'



