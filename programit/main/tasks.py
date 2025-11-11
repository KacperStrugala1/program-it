from celery import shared_task
from django.utils import timezone
from datetime import timedelta
from .models import Time

@shared_task
def add_points_to_active_timers():

    now = timezone.now()
    timers = Time.objects.filter(is_active=True)

    for timer in timers:
        if now >= timer.end_time:
            
            elapsed = now - timer.end_time
            intervals = int(elapsed.total_seconds() // 30)  # 30 sec intervals   
            new_points = intervals * 20

            if new_points > timer.points:
                timer.points = new_points
                timer.save()
                print(f" {timer.user.username}: +{new_points} pkt")
                print("Points updated for active timers.")
        else:
            Time.objects.exclude(pk=timer.pk).update(is_active=False)
            print(f"{timer.user.username}: No new points to add.")