class VaccineError(Exception):
    pass


class NotVaccinatedError(VaccineError):
    def __init__(self) -> None:
        self.message = "Данные о вакцинации не найдены"
        super().__init__(self.message)


class OutdatedVaccineError(VaccineError):
    def __init__(self) -> None:
        self.message = "Вакцинация просрочена"
        super().__init__(self.message)


class NotWearingMaskError(Exception):
    def __init__(self) -> None:
        self.message = "Отсуствует маска"
        super().__init__(self.message)
