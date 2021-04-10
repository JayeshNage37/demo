from django.db import models
from django.utils import timezone
from datetime import time

# Create your models here.
class DriverLeaves(models.Model):
    driver_leave_id = models.CharField(max_length = 256)
    owner_id = models.CharField(max_length = 256, null = True)
    driver_id = models.CharField(max_length = 256, null = True)
    leave_type = models.CharField(max_length = 256, null = True)
    start_date = models.DateField()
    end_date = models.DateField()
    leave_reason = models.TextField(null = True)
    leave_status = models.TextField(null = True)
    no_of_days= models.CharField(max_length=256, null = True)
    updated_at = models.DateTimeField()
    updated_by = models.CharField(max_length = 256, null = True)
    created_at = models.DateTimeField()
    created_by = models.CharField(max_length = 256, null = True)
    is_deleted = models.BooleanField(default = False)
    branch_id = models.CharField(max_length = 256,null = True)
    fleet_id = models.CharField(max_length = 256, null = True)
    rejection_reason = models.TextField(null = True)
    class Meta():
        db_table = 'driver_leaves'
        indexes = [
            models.Index(fields=['driver_id',]),
            
        ]

    
    # DESCRIPTION: This function apply driver leaves   
    @classmethod
    def create_driver_leave(cls,driver_leaves_dict):
        try:
            driver_leave_object = DriverLeaves()
            driver_leave_object.driver_leave_id =  "DL"+str(int(time.time_ns() * 10))
            if 'driver_id' in driver_leaves_dict and driver_leaves_dict['driver_id']!="":
                driver_leave_object.driver_id = driver_leaves_dict['driver_id']
            if 'leave_type' in driver_leaves_dict and driver_leaves_dict['leave_type']!="":
                driver_leave_object.leave_type = driver_leaves_dict['leave_type']
            if 'start_date' in driver_leaves_dict and driver_leaves_dict['start_date']!="":
                driver_leave_object.start_date = driver_leaves_dict['start_date']
            if 'end_date' in driver_leaves_dict and driver_leaves_dict['end_date']!="":
                driver_leave_object.end_date = driver_leaves_dict['end_date']
            if 'leave_reason' in driver_leaves_dict and driver_leaves_dict['leave_reason']!="":
                driver_leave_object.leave_reason = driver_leaves_dict['leave_reason']
            if 'leave_status' in driver_leaves_dict and driver_leaves_dict['leave_status']!="":
                driver_leave_object.leave_status = "Pending"
            if 'no_of_days' in driver_leaves_dict and driver_leaves_dict['no_of_days']!="":
                driver_leave_object.no_of_days = driver_leaves_dict['no_of_days']
            if 'created_by' in driver_leaves_dict and driver_leaves_dict['created_by']!="":
                driver_leave_object.created_by = driver_leaves_dict['created_by']
            driver_leave_object.created_at = timezone.now()
            if 'updated_by' in driver_leaves_dict and driver_leaves_dict['updated_by']!="":
                driver_leave_object.updated_by = driver_leaves_dict['updated_by']
            driver_leave_object.updated_at = timezone.now()
            if 'fleet_id' in driver_leaves_dict and driver_leaves_dict['fleet_id']!="":
                driver_leave_object.fleet_id = driver_leaves_dict['fleet_id']
            if 'branch_id' in driver_leaves_dict and driver_leaves_dict['branch_id']!="":
                driver_leave_object.branch_id = driver_leaves_dict['branch_id']
            if 'driver_leaves_url' in driver_leaves_dict and driver_leaves_dict['driver_leaves_url']!="":
                driver_leave_object.driver_leaves_url = driver_leaves_dict['driver_leaves_url']
            driver_leave_object.save()
            return True    
        except (Exception) as error:
            print(error)
            return False       
