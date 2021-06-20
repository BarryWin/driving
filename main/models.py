from django.db import models



class Ucheniki(models.Model):
    name = models.CharField('Имя', max_length=250)
    fam = models.CharField('Фамилия', max_length=250)
    otch = models.CharField('Отчество', max_length=250, null=True)
    fioUch = models.CharField('ФИО', max_length=60)
    address = models.CharField('Адрес проживания', max_length=250)
    tel = models.CharField('Телефон', max_length=20)
    email = models.CharField('Электронынй адрес', max_length=150)
    photo = models.CharField('Фотография', max_length=150)
    gruppa = models.CharField('Группа', max_length=10, default='')
    date_rogd = models.DateField('Дата рождения')


    def __str__(self):
        return self.fioUch

    def get_absolute_url(self):
        return f'/avtoschool/{self.id}'

    class Meta:
        verbose_name = 'Ученики'
        verbose_name_plural = 'Ученики'

class Sotrudniki(models.Model):
    name = models.CharField('Имя', max_length=250)
    fam = models.CharField('Фамилия', max_length=250)
    otch = models.CharField('Отчество', max_length=250, null=True)
    fioSotr = models.CharField('ФИО', max_length=250)
    tel = models.CharField('Телефон', max_length=20)
    email = models.CharField('Электронный адрес', max_length=150)
    photo = models.CharField('Фотография', max_length=150)
    date_rogd = models.DateField('Дата рождения')
    dolgn = models.CharField('Должность', max_length=60)
    ucheniki = models.TextField('Ученики', max_length=500)

    def __str__(self):
        return self.fioSotr

    def get_absolute_url(self):
        return f'/avtoschool/{self.id}'

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'


class Chat(models.Model):
    fioUch = models.ForeignKey(Ucheniki, on_delete=models.PROTECT, verbose_name='Фио ученика')
    fioSotr = models.ForeignKey(Sotrudniki, on_delete=models.PROTECT, verbose_name='Фио сотрудника')

    def __str__(self):
        return self.fioUch, self.fioSotr

    def get_absolute_url(self):
        return f'/avtoschool/{self.id}'

    class Meta:
        verbose_name = 'Чат'
        verbose_name_plural = 'Чаты'


class Message(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, verbose_name='Чат')
    message = models.TextField('Сообщение')
    created_at = models.DateTimeField('Дата и время сообщения')

    def __str__(self):
        return self.chat_id

    def get_absolute_url(self):
        return f'/avtoschool/{self.id}'

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщение'


class DrivingCard(models.Model):
    date = models.DateTimeField('Дата занятия')
    dlitelnost = models.FloatField('Продолжительность')
    hoursleft = models.FloatField('Осталось часов')
    fioSotr = models.ForeignKey(Sotrudniki, on_delete=models.PROTECT, verbose_name='Фио сотрудника')
    fioUch = models.ForeignKey(Ucheniki, on_delete=models.PROTECT, verbose_name='Фио ученика')
    comment = models.CharField('Комментарий инструктора', max_length=250)

    def __str__(self):
        return self.comment

    def get_absolute_url(self):
        return f'/avtoschool/{self.id}'

    class Meta:
        verbose_name = 'Карточка вождения'
        verbose_name_plural = 'Карточки вождения'


class Tranport(models.Model):
    gosnomer = models.CharField('Гос.Номер', max_length=60)
    nazvavto = models.CharField('Макрка, модель', max_length=20)
    tip_transm = models.CharField('Тип трансмиссии', max_length=20)
    categ = models.CharField('Категория', max_length=5)
    fioSotr = models.ForeignKey(Sotrudniki, on_delete=models.PROTECT, verbose_name='Фио сотрудника')

    def __str__(self):
        return self.nazvavto

    def get_absolute_url(self):
        return f'/avtoschool/{self.id}'

    class Meta:
        verbose_name = 'Справочник транспорта'
        verbose_name_plural = 'Справочник трансопрта'


class Trvperiod(models.Model):
    fioUch = models.ForeignKey(Ucheniki, on_delete=models.PROTECT, verbose_name='Фио ученика')
    fioSotr = models.ForeignKey(Sotrudniki, on_delete=models.PROTECT, verbose_name='Фио сотрудника')
    gosnomer = models.ForeignKey(Tranport, on_delete=models.PROTECT, verbose_name='Госномер')

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
    nach_obuch = models.DateField('Начало обучения')
    konec_obuch = models.DateField('Конец обучения')

    def __str__(self):
        return self.nazv

    def get_absolute_url(self):
        return f'/avtoschool/{self.id}'

    class Meta:
        verbose_name = 'Список групп'
        verbose_name_plural = 'Списки групп'


class Otchet(models.Model):
    nazv = models.ForeignKey(Group, on_delete=models.PROTECT, verbose_name='Номер группы', default='')
    datenach = models.DateField('Дата начала обучения', max_length=20)
    kolvo = models.CharField('Количество челвоек', max_length=20)
    kolvozdav = models.CharField('Количесвто сдавших экзамен', max_length=20)
    sotrud = models.CharField('Сотрудники', max_length=20)


    def __str__(self):
        return self.nazv

    def get_absolute_url(self):
        return f'/avtoschool/{self.id}'

    class Meta:
        verbose_name = 'Отчет'
        verbose_name_plural = 'Отчет'


class Vedomost(models.Model):
    nomer_vedomost = models.IntegerField('Номер ведомости')
    date_vedomost = models.DateField('Дата создания ведомости')
    fioSotr = models.ForeignKey(Sotrudniki, on_delete=models.PROTECT, verbose_name='ФИО сотрудника')

    def __str__(self):
        return self.nomer_vedomost

    def get_absolute_url(self):
        return f'/avtoschool/{self.id}'

    class Meta:
        verbose_name = 'Ведомость'
        verbose_name_plural = 'Ведомости'


class PosVedomost(models.Model):
    nomer_vedomost = models.ForeignKey(Vedomost, on_delete=models.PROTECT, verbose_name='Позиция ведомости')
    fioUch = models.ForeignKey(Ucheniki, on_delete=models.PROTECT, verbose_name='Фио ученика')
    result = models.CharField('Результат', max_length=20)


class Dogovor(models.Model):
    nomerdog = models.CharField('Номер договора', max_length=20)
    datesost = models.DateField()
    stoimostobuch = models.PositiveIntegerField('Стоимость обучения')

    categ = models.ForeignKey(Progobuch, on_delete=models.PROTECT)

    fioUch = models.ForeignKey(Ucheniki, on_delete=models.PROTECT)

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


class Rasp_teor(models.Model):
    date_zan = models.DateTimeField('Дата занятия')
    fioSotr = models.ForeignKey(Sotrudniki, on_delete=models.PROTECT, verbose_name='Фио сотрудника')
    nazv = models.ForeignKey(Group, on_delete=models.PROTECT, verbose_name='Группа', default='')
    tema = models.CharField('Тема занятия', max_length=250, default='')
    status = models.CharField('Статус', max_length=20)

    def __str__(self):
        return self.status

    def get_absolute_url(self):
        return f'/avtoschool/{self.id}'

    class Meta:
        verbose_name = 'Расписание теоретических занятий'
        verbose_name_plural = 'Расписание теоретических занятий'


class Rasp_praktiki(models.Model):
    date_zan = models.DateTimeField('Дата занятия')
    fioSotr = models.ForeignKey(Sotrudniki, on_delete=models.PROTECT, verbose_name='ФИО сотрудника')
    fioUch = models.ForeignKey(Ucheniki, on_delete=models.PROTECT, verbose_name='ФИО ученика')
    tema = models.CharField('Тема занятия', max_length=250, default='')
    status = models.CharField('Статус', max_length=20)

    def __str__(self):
        return self.tema

    def get_absolute_url(self):
        return f'/avtoschool/{self.id}'

    class Meta:
        verbose_name = 'Расписание практических занятий'
        verbose_name_plural = 'Расписание практических занятий'


class Zurnal(models.Model):
    nomer_zurnal = models.CharField('Номер Журнала', max_length=20, default='')
    nazv = models.ForeignKey(Group, on_delete=models.PROTECT)
    date_otkr = models.DateField('Дата открытия')

    def __str__(self):
        return self.nazv

    def get_absolute_url(self):
        return f'/avtoschool/{self.id}'

    class Meta:
        verbose_name = 'Журнал'
        verbose_name_plural = 'Журналы'


class PosZurnal(models.Model):
    nomer_zurnal = models.ForeignKey(Zurnal, on_delete=models.PROTECT)
    otmetka_pos = models.CharField('Посещаемость', max_length=20)
    fioUch = models.ForeignKey(Ucheniki, on_delete=models.PROTECT, verbose_name='Фио ученика')
    date_zan = models.ForeignKey(Rasp_teor, on_delete=models.PROTECT, verbose_name='Дата занятия')

    def __str__(self):
        return self.fioUch

    def get_absolute_url(self):
        return f'/avtoschool/{self.id}'

    class Meta:
        verbose_name = 'Позиция журнала'
        verbose_name_plural = 'Позиции журнала'


class Documenti(models.Model):
    viddoc = models.CharField('Вид документа', max_length=100)
    datedoc = models.CharField('Дата выдачи документа', max_length=100)
    nomerdoc = models.CharField('Номер', max_length=100)
    seriadoc = models.CharField('Серия', max_length=100)
    kemvidan = models.CharField('Кем выдан', max_length=100)
    opisandoc = models.CharField('Описание документа', max_length=100)
    fioUch = models.ForeignKey(Ucheniki, on_delete=models.PROTECT, default='')
    copy_doc = models.CharField('Копия документа', max_length=100, default='')

    # fiouch = models.CharField('фио', max_length=100)

    def __str__(self):
        return self.fioUch

    def get_absolute_url(self):
        return f'/avtoschool/{self.id}'

    class Meta:
        verbose_name = 'Документ'
        verbose_name_plural = 'Документы'



