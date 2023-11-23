from flask import Blueprint, render_template, current_app, jsonify

main_blueprint = Blueprint('main', __name__)

@main_blueprint.route('/')
def index():
    calendar_service = current_app.config["CALENDAR_SERVICE"]
    calendar_id = current_app.config["CALENDAR_ID"]

    # Fetch events from the calendar
    events = calendar_service.events().list(
        calendarId=calendar_id,
        timeMin='2023-01-01T00:00:00Z',  # Adjust the start time as needed
        maxResults=10,
        singleEvents=True,
        orderBy='startTime'
    ).execute()

    # Extract relevant information from events
    event_data = []
    for event in events.get('items', []):
        event_data.append({
            'summary': event['summary'],
            'start_time': event['start'].get('dateTime', event['start'].get('date')),
            'end_time': event['end'].get('dateTime', event['end'].get('date'))
        })

    return render_template('index.html', events=event_data)

@main_blueprint.route('/api/calendar-events')
def get_calendar_events():
    calendar_service = current_app.config["CALENDAR_SERVICE"]
    calendar_id = current_app.config["CALENDAR_ID"]

    events = calendar_service.events().list(calendarId=calendar_id).execute()
    return jsonify(events.get('items', []))
