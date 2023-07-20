from django.db import models
from django.db.models import Count

class ReunionManager(models.Manager):

    def reuniones_by_job(self):
        #utilizando groupBy
        result = self.values('persona__job').annotate(
            cantidad=Count('id')
        )
        print(result)
        return result
