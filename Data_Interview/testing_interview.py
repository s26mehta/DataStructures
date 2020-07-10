#

# Interviewer
#  - work_start : datetime
#  - work_end : datetime
#  - booked_events: Event[]
# Event:
#  - start_time: datetime
#  - duration: int # seconds
# Interviewer.book()


from datetime import datetime, date
import unittest

class Event:
  def __init__(self, start_time, duration):
    self.start_time = start_time
    self.duration = duration

class Interviewer:
  def __init__(self, start_work, end_work):
    self.work_start = start_work
    self.work_end = end_work
    self.booked_events = {}

  def book_event(self, event):
    date = str(event.start_time.date())
    start_timestamp = event.start_time.timestamp()
    end_timestamp = start_timestamp+event.duration
    if date in self.booked_events:
      date_events_list = self.booked_events[date].keys()

      # check for collisions
      collision_detected = False
      for cur_event in date_events_list:
        cur_event_start = cur_event[0]
        cur_event_end = cur_event[1]
        if start_timestamp >= cur_event_start and start_timestamp <= cur_event_end:
          collision_detected = True
        if end_timestamp >= cur_event_start and end_timestamp <= cur_event_end:
          collision_detected = True

      if collision_detected:
        raise ValueError("Trying to book an event, during an existing event. Please choose a different time.")
      else:
        self.booked_events[date][(start_timestamp, end_timestamp)] = event
        return True
    else:
      self.booked_events[date] = {(start_timestamp, end_timestamp): event}
      return True

class TestMethods(unittest.TestCase):
  def test_initialize_interviewer(self):
    start_work = datetime(2019, 10, 4, 9, 0, 0)
    end_work = datetime(2019, 10, 4, 17, 0, 0)
    interviewer_1 = Interviewer(start_work, end_work)
    self.assertEqual(interviewer_1.work_start, start_work)
    self.assertEqual(interviewer_1.work_end, end_work)
    self.assertEqual(interviewer_1.booked_events, {})

  def test_add_first_event(self):
    start_work = datetime(2019, 10, 4, 9, 0, 0)
    end_work = datetime(2019, 10, 4, 17, 0, 0)
    interviewer_1 = Interviewer(start_work, end_work)

    hour_in_sec = 1*60*60
    event = Event(datetime(2019, 10, 4, 9, 0, 0), hour_in_sec)
    start_timestamp = event.start_time.timestamp()
    end_timestamp = start_timestamp + event.duration
    result = interviewer_1.book_event(event)
    self.assertEqual(result, True)
    self.assertEqual(interviewer_1.booked_events, {str(event.start_time.date()): {(start_timestamp, end_timestamp): event}})

  def test_collision(self):
    start_work = datetime(2019, 10, 4, 9, 0, 0)
    end_work = datetime(2019, 10, 4, 17, 0, 0)
    interviewer_1 = Interviewer(start_work, end_work)

    hour_in_sec = 1*60*60
    event = Event(datetime(2019, 10, 4, 9, 0, 0), hour_in_sec)
    interviewer_1.book_event(event)

    event1 = Event(datetime(2019,10,4,9,30,0), hour_in_sec)
    with self.assertRaises(ValueError):
      interviewer_1.book_event(event1)


if __name__ == '__main__':
  unittest()




