import React, { useEffect, useState } from 'react';

const CalendarApp = () => {
  const [events, setEvents] = useState([]);

  useEffect(() => {
    const fetchCalendarEvents = async () => {
      try {
        const response = await fetch('http://localhost:5000/api/calendar-events');
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        const data = await response.json();
        setEvents(data);
      } catch (error) {
        console.error('Error fetching calendar events:', error);
      }
    };

    fetchCalendarEvents();
  }, []);

  return (
    <div>
      <p>see who's staying with us</p>
      <iframe src="https://calendar.google.com/calendar/embed?height=600&wkst=1&bgcolor=%23ffffff&ctz=America%2FNew_York&showTitle=0&showDate=1&showPrint=0&showCalendars=1&mode=MONTH&src=MmI1YWZmNzg3OGQ2MzIzZDVhOTc5ZTg5NGFmYWExNGMyNTZkODVmYTViMWY4OWYwMGExNzIyYmI4MmU4ZjBlOEBncm91cC5jYWxlbmRhci5nb29nbGUuY29t&color=%23A79B8E" style={{ border: 'solid 1px #777' }} width="800" height="600" frameborder="0" scrolling="no"></iframe>
      <p>upcoming stays:</p>
      <ul>
        {events.map((event) => (
          <li key={event.id}>{event.summary} - { event.start_time } to { event.end_time } </li>
        ))}
      </ul>
    </div>
  );
};

export default CalendarApp;
