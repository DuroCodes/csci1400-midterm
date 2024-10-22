from dataclasses import dataclass


@dataclass
class Question:
    question: str
    options: list[str]
    correct_answer: int


questions = [
    Question(
        question="What is the most common cause of CPU overheating?",
        options=[
            "Insufficient storage",
            "Faulty RAM",
            "Outdated drivers",
            "Dust buildup",
        ],
        correct_answer=3,
    ),
    Question(
        question="What is a common symptom of a memory leak?",
        options=["Overheating", "No sound", "Screen flickering", "Slow performance"],
        correct_answer=3,
    ),
    Question(
        question="What should you check first when a storage device is not recognized?",
        options=[
            "Power supply",
            "Graphics card",
            "Driver updates",
            "Cable connections",
        ],
        correct_answer=3,
    ),
    Question(
        question="Which issue can cause sudden power supply failure?",
        options=[
            "Corrupted OS",
            "Overloading the PSU",
            "Incompatible graphics card",
            "Faulty RAM",
        ],
        correct_answer=1,
    ),
    Question(
        question="What is a common indication of a graphics card malfunction?",
        options=[
            "No power",
            "Incompatible software",
            "Slow internet speed",
            "Strange artifacts on screen",
        ],
        correct_answer=3,
    ),
    Question(
        question="What can be a symptom of an operating system conflict?",
        options=[
            "Slow performance",
            "Frequent crashes",
            "Poor graphics quality",
            "Connection issues",
        ],
        correct_answer=1,
    ),
    Question(
        question="What is a typical sign of driver incompatibility?",
        options=[
            "No internet connection",
            "Device not functioning",
            "Slow loading times",
            "Overheating",
        ],
        correct_answer=1,
    ),
    Question(
        question="What could be a possible cause of intermittent networking issues?",
        options=[
            "Insufficient RAM",
            "Incompatible software",
            "Faulty cables",
            "Outdated drivers",
        ],
        correct_answer=2,
    ),
    Question(
        question="What is a common issue with peripheral devices?",
        options=[
            "CPU overheating",
            "Power supply issues",
            "Insufficient storage",
            "Incorrect driver installation",
        ],
        correct_answer=3,
    ),
    Question(
        question="What is a primary symptom of a security breach?",
        options=[
            "Unusual account activity",
            "Slow performance",
            "Driver issues",
            "Overheating",
        ],
        correct_answer=0,
    ),
    Question(
        question="What is the first step to take when your computer won't boot?",
        options=[
            "Replace the RAM",
            "Run a virus scan",
            "Check the power connection",
            "Reinstall the OS",
        ],
        correct_answer=2,
    ),
    Question(
        question="Which of the following can lead to memory problems?",
        options=[
            "Running too many applications",
            "Using a powerful CPU",
            "Upgrading the graphics card",
            "Cleaning the hard drive",
        ],
        correct_answer=0,
    ),
    Question(
        question="What is a potential sign of hard drive failure?",
        options=[
            "Increased RAM usage",
            "Strange clicking sounds",
            "High internet speeds",
            "Clear display",
        ],
        correct_answer=1,
    ),
    Question(
        question="Which power supply rating is most important for stability?",
        options=[
            "Color",
            "Brand",
            "Wattage",
            "Form factor",
        ],
        correct_answer=2,
    ),
    Question(
        question="What is a common fix for a graphics card that is not detected?",
        options=[
            "Running a malware scan",
            "Re-seating the card",
            "Updating the OS",
            "Checking RAM slots",
        ],
        correct_answer=1,
    ),
    Question(
        question="What could cause a blue screen of death (BSOD)?",
        options=[
            "Outdated web browser",
            "Too much RAM",
            "Faulty hardware",
            "Not enough storage",
        ],
        correct_answer=2,
    ),
    Question(
        question="What is an indication that you need to update your drivers?",
        options=[
            "Enhanced performance",
            "Increased storage space",
            "Device not functioning as expected",
            "New hardware installation",
        ],
        correct_answer=2,
    ),
    Question(
        question="Which of the following might indicate a network issue?",
        options=[
            "No audio output",
            "High CPU usage",
            "Slow internet speeds",
            "Frequent crashes",
        ],
        correct_answer=2,
    ),
    Question(
        question="What is a common issue with printers?",
        options=[
            "Low disk space",
            "Paper jams",
            "Overheating CPU",
            "Slow internet connection",
        ],
        correct_answer=1,
    ),
    Question(
        question="What could be a sign of malware on your computer?",
        options=[
            "Faster internet speeds",
            "Better graphics quality",
            "More available storage",
            "Unexpected pop-ups",
        ],
        correct_answer=3,
    ),
    Question(
        question="What is the main purpose of a CPU cooler?",
        options=[
            "To enhance graphics quality",
            "To prevent overheating",
            "To increase RAM speed",
            "To boost performance",
        ],
        correct_answer=1,
    ),
    Question(
        question="What can cause a computer to freeze?",
        options=[
            "Too many updates",
            "High storage capacity",
            "Insufficient RAM",
            "Clean OS installation",
        ],
        correct_answer=2,
    ),
    Question(
        question="What might indicate that a power supply is failing?",
        options=[
            "Low battery",
            "Random shutdowns",
            "Slow performance",
            "Increased fan noise",
        ],
        correct_answer=1,
    ),
    Question(
        question="What can you check if your graphics card is overheating?",
        options=[
            "Fan operation",
            "Storage capacity",
            "Power supply rating",
            "Operating system version",
        ],
        correct_answer=0,
    ),
    Question(
        question="What is a symptom of an incompatible software installation?",
        options=[
            "Increased RAM",
            "Better graphics",
            "Error messages",
            "Improved speed",
        ],
        correct_answer=2,
    ),
    Question(
        question="What is an effective method for diagnosing network problems?",
        options=[
            "Driver updates",
            "Defragmentation",
            "Ping test",
            "Disk cleanup",
        ],
        correct_answer=2,
    ),
    Question(
        question="What common issue can arise with USB devices?",
        options=[
            "Too much RAM",
            "No power supply issues",
            "Device not recognized",
            "Slow processing speed",
        ],
        correct_answer=2,
    ),
    Question(
        question="Which of the following can help secure your computer against malware?",
        options=[
            "Upgrading the CPU",
            "Increasing storage space",
            "Installing antivirus software",
            "Adding more RAM",
        ],
        correct_answer=2,
    ),
    Question(
        question="What is an indicator that your computer might be infected with malware?",
        options=[
            "Faster processing speed",
            "High disk space",
            "Sluggish performance",
            "Improved graphics",
        ],
        correct_answer=2,
    ),
    Question(
        question="What can be a sign of a failing hard drive?",
        options=[
            "Higher graphics quality",
            "Increased performance",
            "Frequent error messages",
            "Reduced power usage",
        ],
        correct_answer=2,
    ),
    Question(
        question="What is the first thing to check if your system crashes unexpectedly?",
        options=[
            "Software updates",
            "Event Viewer logs",
            "Disk space",
            "RAM size",
        ],
        correct_answer=1,
    ),
    Question(
        question="What could cause issues with multiple peripherals?",
        options=[
            "Excess RAM",
            "Insufficient power supply",
            "Updated drivers",
            "Clean OS installation",
        ],
        correct_answer=1,
    ),
    Question(
        question="What is a common effect of overheating?",
        options=[
            "Increased RAM",
            "System instability",
            "Better graphics performance",
            "More available storage",
        ],
        correct_answer=1,
    ),
]
