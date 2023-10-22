import time

class MeditationSession:
    def __init__(self, name, duration):
        self.name = name
        self.duration = duration

    def start_session(self):
        print(f"Starting {self.name} session...")
        time.sleep(self.duration)
        print(f"{self.name} session complete.")

class MeditationApp:
    def __init__(self):
        self.sessions = []

    def add_session(self, session):
        self.sessions.append(session)

    def display_sessions(self):
        print("Available Sessions:")
        for i, session in enumerate(self.sessions, start=1):
            print(f"{i}. {session.name}")

    def start_app(self):
        while True:
            self.display_sessions()
            choice = input("Enter the number of the session you want to start (q to quit): ")
            if choice == 'q':
                break
            try:
                choice = int(choice) - 1
                if 0 <= choice < len(self.sessions):
                    self.sessions[choice].start_session()
                else:
                    print("Invalid session number. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    app = MeditationApp()

    # Add sessions
    session1 = MeditationSession("Breathing Exercise", 300)  # 5 minutes
    session2 = MeditationSession("Body Scan", 600)  # 10 minutes

    app.add_session(session1)
    app.add_session(session2)

    app.start_app()
