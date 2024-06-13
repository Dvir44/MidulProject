class PlannerHelper:
    """
    A helper class for the planner to access information that is useful for planning.
    Only information provided via this class can be used for planning.
    Other information that the competition participant wants to use, must be constructed via the planner's report method.
    """

    def __init__(self, problem):
        self.__problem = problem

    def available_resources(self, resource_type):
        """
        Returns the number of resources of a specific type that are available.
        Possible types are "OR", "A_BED", "B_BED".
        :param resource_type: the type of resources to check for availability.
        :return: the number of available resources.
        """
        return self.__problem.available_resources(resource_type)

    def get_case_type(self, case_id):
        """
        Returns the type of the case with the given id.
        :param case_id: the id of the case.
        :return: the type of the case.
        """
        return self.__problem.get_case_type(case_id)

    def get_case_data(self, case_id):
        """
        Returns the data of the case with the given id.
        :param case_id: the id of the case.
        :return: the data of the case, which is a dictionary of data types to data values.
        """
        return self.__problem.get_case_data(case_id)