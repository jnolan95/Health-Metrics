from metrics.fitbit_metrics.fitbit_metric_class import FitbitMetric


class BodyWeight(FitbitMetric):
    def __init__(self, calendar_data):
        self.resource = "body/weight"
        super().__init__(calendar_data)
        self.df = self.df.rename(columns={"value": "Weight"})
        self.df["Weight"] = [int(float(weight)) for weight in self.df["Weight"]]




class BodyFat(FitbitMetric):
    def __init__(self, calendar_data):
        self.resource = "body/fat"
        super().__init__(calendar_data)
        self.df = self.df.rename(columns={"value": "Body Fat %"})
        self.df["Body Fat %"] = [int(float(weight)) for weight in self.df["Body Fat %"]]
