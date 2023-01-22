class PlanNotFoundError(Exception):
    message = "The plan you specified does not exist."

    def __str__(self):
        return PlanNotFoundError.message