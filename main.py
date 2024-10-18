import time
import random
import os
import psutil
from colorama import init, Fore, Style
import string

# Initialize colorama
init(autoreset=True)


def get_system_info():
    cpu = psutil.cpu_percent(interval=0.1)
    mem = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent
    return cpu, mem, disk


def output_data_point():
    data_points = [
        'Quantum Flux',
        'Neutrino Emissions',
        'Plasma Levels',
        'Subspace Anomalies',
        'Warp Field Integrity',
        'Ionization Rates',
        'Graviton Flux Density',
        'Chroniton Particle Count',
        'Zero Point Energy',
        'Tachyon Signal Strength'
    ]

    units = ['%', 'units', 'MΩ', 'kPa', 'μSv', 'GHz', 'Tesla', 'Joules', 'Kelvin', 'Parsecs']

    colors = [Fore.RED, Fore.GREEN, Fore.BLUE, Fore.YELLOW, Fore.CYAN, Fore.MAGENTA]

    data = random.choice(data_points)
    unit = random.choice(units)
    color = random.choice(colors)
    value = round(random.uniform(0, 1000), 2)
    print(f"{color}{data}: {value} {unit}")


def output_long_text():
    messages = [
        "Initializing quantum field parameters for subspace distortion analysis. This process may take several moments as we calibrate the tachyon emitters and align the deflector dish to the precise harmonics required.",
        "Analyzing sensor data from the last warp jump. Graviton readings are off the charts, suggesting a possible encounter with a micro-singularity. Further investigation is recommended to ensure warp field stability.",
        "Compiling diagnostic reports on the ion propulsion system. Recent fluctuations in plasma conduits could indicate a need for recalibration of the magnetic containment fields.",
        "Decoding encrypted signals intercepted from an unknown source. Preliminary analysis suggests a complex algorithm involving quantum cryptography and subspace frequency modulation.",
        "Monitoring cosmic background radiation levels to detect anomalies that could signify wormhole formations or other astrophysical phenomena of interest."
    ]

    colors = [Fore.LIGHTRED_EX, Fore.LIGHTGREEN_EX, Fore.LIGHTBLUE_EX, Fore.LIGHTYELLOW_EX, Fore.LIGHTCYAN_EX, Fore.LIGHTMAGENTA_EX]

    message = random.choice(messages)
    color = random.choice(colors)
    print(f"{color}{message}")


def output_table():
    headers = ["Parameter", "Value", "Unit"]
    parameters = [
        ("CPU Usage", f"{psutil.cpu_percent()}%", ""),
        ("Memory Usage", f"{psutil.virtual_memory().percent}%", ""),
        ("Disk Usage", f"{psutil.disk_usage('/').percent}%", ""),
        ("Network Sent", f"{psutil.net_io_counters().bytes_sent / (1024*1024):.2f}", "MB"),
        ("Network Received", f"{psutil.net_io_counters().bytes_recv / (1024*1024):.2f}", "MB"),
        ("Active Processes", f"{len(psutil.pids())}", ""),
        ("System Uptime", f"{int(time.time() - psutil.boot_time()) // 3600}", "hours"),
        ("Temperature", f"{random.uniform(30, 90):.2f}", "°C"),
        ("Fan Speed", f"{random.randint(1000, 5000)}", "RPM")
    ]

    colors = [Fore.WHITE, Fore.LIGHTBLACK_EX]
    color = random.choice(colors)

    # Print table header
    header_line = f"{color}{headers[0]:<20}{headers[1]:<15}{headers[2]:<10}"
    print(header_line)
    print(f"{color}{'-'*45}")

    # Print table rows
    for param in parameters:
        line = f"{color}{param[0]:<20}{param[1]:<15}{param[2]:<10}"
        print(line)


def output_random_event():
    events = [
        "WARNING: Unidentified vessel detected on long-range scanners.",
        "SIMULATED ALERT: Simulated Warp core breach imminent. Simulating emergency protocols.",
        "NOTICE: Life support systems operating at maximum efficiency.",
        "UPDATE: New software patch available for the navigation system.",
        "MESSAGE: Incoming transmission from fleet Command."
    ]

    colors = [Fore.RED + Style.BRIGHT, Fore.YELLOW + Style.BRIGHT, Fore.CYAN + Style.BRIGHT]

    event = random.choice(events)
    color = random.choice(colors)
    print(f"{color}{event}")


def output_encrypted_transmission():
    colors = [Fore.WHITE, Fore.LIGHTBLACK_EX, Fore.LIGHTBLUE_EX]
    color = random.choice(colors)
    length = random.randint(100, 4096)
    # Generate a random string with interesting characters
    characters = string.ascii_letters + string.digits + string.punctuation
    encrypted_message = ''.join(random.choice(characters) for _ in range(length))
    print(f"{color}Encrypted Transmission Received:\n{encrypted_message}")


def output_decryption_attempt():
    colors = [Fore.YELLOW, Fore.LIGHTGREEN_EX]
    color = random.choice(colors)
    decryption_keys = [''.join(random.choices(string.ascii_uppercase + string.digits, k=16)) for _ in range(5)]
    print(f"{color}Attempting to decrypt message...")
    for key in decryption_keys:
        print(f"{color}Trying key: {key}")
        time.sleep(random.uniform(0.2, 0.5))
    success = random.choice([True, False])
    if success:
        decrypted_messages = [
            "Coordinates received. Rendezvous at sector 7G.",
            "Encryption bypassed. Accessing mainframe...",
            "Transmission decoded. Awaiting further instructions.",
            "Secure channel established. Commencing data upload."
        ]
        message = random.choice(decrypted_messages)
        print(f"{color}Decryption Successful!\nDecrypted Message: '{message}'\n")
    else:
        print(f"{color}Decryption Failed. Further attempts required.\n")


def output_star_map_coordinates():
    colors = [Fore.LIGHTCYAN_EX, Fore.LIGHTBLUE_EX]
    color = random.choice(colors)
    sectors = ['Alpha', 'Beta', 'Gamma', 'Delta', 'Epsilon', 'Zeta', 'Eta', 'Theta', 'Iota', 'Kappa']
    celestial_objects = ['Nebula', 'Black Hole', 'Supernova', 'Quasar', 'Pulsar', 'Red Dwarf', 'Binary Star', 'Exoplanet', 'Asteroid Belt', 'Comet']
    sector = random.choice(sectors)
    x = round(random.uniform(-1000, 1000), 2)
    y = round(random.uniform(-1000, 1000), 2)
    z = round(random.uniform(-1000, 1000), 2)
    object_name = random.choice(celestial_objects)
    distance = round(random.uniform(1, 10000), 2)
    unit = random.choice(['light-years', 'parsecs'])
    print(f"{color}Star Map Data:")
    print(f"{color}Sector {sector} Coordinates: X={x}, Y={y}, Z={z}")
    print(f"{color}Object Detected: {object_name}")
    print(f"{color}Distance from current position: {distance} {unit}")


def output_algorithm_processing():
    colors = [Fore.LIGHTMAGENTA_EX, Fore.LIGHTGREEN_EX]
    color = random.choice(colors)
    algorithms = [
        'Quantum Entanglement Solver',
        'Subspace Frequency Modulator',
        'Temporal Paradox Resolver',
        'Gravitational Wave Analyzer',
        'Warp Field Stabilizer',
        'Nanite Swarm Optimization',
        'Artificial Intelligence Core Boot',
        'Dark Matter Density Calculator',
        'Neural Network Matrix Reconfiguration',
        'Zero Point Energy Extractor'
    ]
    algorithm = random.choice(algorithms)
    print(f"{color}Executing {algorithm}...")
    total_steps = random.randint(3, 7)
    for step in range(1, total_steps + 1):
        progress = int((step / total_steps) * 100)
        print(f"{color}Processing... {progress}% complete")
        time.sleep(random.uniform(0.5, 1.0))
    results = [
        'Calculation complete. Results stored in database.',
        'Process successful. No anomalies detected.',
        'Optimization finished. Performance increased by 12%.',
        'Analysis complete. Further action recommended.',
        'Operation successful. System stability ensured.'
    ]
    result = random.choice(results)
    print(f"{color}{result}")


def output_anomaly_detection():
    colors = [Fore.LIGHTRED_EX, Fore.YELLOW, Fore.LIGHTYELLOW_EX]
    color = random.choice(colors)
    anomalies = [
        'Power fluctuation detected in sector 4.',
        'Shield harmonic variance exceeds safe parameters.',
        'Life support oxygen levels dropping.',
        'Unidentified object approaching at high velocity.',
        'Communication array interference detected.',
        'Hull breach detected on deck 3.',
        'Temperature anomaly detected in engine core.',
        'Radiation levels exceeding normal limits.',
        'AI core experiencing unexpected behavior.',
        'Temporal distortion detected in local space.'
    ]
    severity_levels = ['Low', 'Medium', 'High', 'Critical']
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    anomaly = random.choice(anomalies)
    severity = random.choice(severity_levels)
    print(f"{color}[{timestamp}] Anomaly Detected: {anomaly}")
    print(f"{color}Severity Level: {severity}")


def output_ai_dialogue():
    colors = [Fore.CYAN, Fore.LIGHTGREEN_EX]
    color = random.choice(colors)
    ai_responses = [
        "All systems are functioning within normal parameters.",
        "Adjusting power output to compensate for engine inefficiency.",
        "Recalculating optimal trajectory based on new data.",
        "Initiating self-diagnostic routines.",
        "Suggesting course correction to avoid asteroid field.",
        "Processing request... Access granted.",
        "Alert: Unauthorized access attempt detected.",
        "Compiling mission report for review.",
        "Performing quantum scan of nearby anomalies.",
        "Awaiting further instructions."
    ]
    user_commands = [
        "Initiate protocol Omega.",
        "Analyze the latest sensor readings.",
        "Run a full diagnostic on all systems.",
        "Prepare the ship for warp speed.",
        "Decrypt the intercepted transmission.",
        "Set a course for the nearest starbase.",
        "Activate the cloaking device.",
        "Engage the automated defense systems.",
        "Begin terraforming procedures.",
        "Compile a list of potential threats."
    ]
    command = random.choice(user_commands)
    response = random.choice(ai_responses)
    print(f"{Fore.LIGHTWHITE_EX}USER: {command}")
    time.sleep(random.uniform(0.5, 1.0))
    print(f"{color}AI: {response}")


def output_system_errors():
    colors = [Fore.RED, Fore.LIGHTRED_EX]
    color = random.choice(colors)
    error_codes = ['0x3F2A', '0x7E21', '0x5D4C', '0x1A3B', '0x9F0E', '0x8B7D', '0x6C5E', '0x2D1F']
    systems = ['Navigation', 'Life Support', 'Engine', 'Communication', 'Weapon', 'Shield', 'Sensor', 'AI Core']
    error_messages = [
        'System overload detected.',
        'Critical failure in subsystem.',
        'Component overheating.',
        'Data corruption encountered.',
        'Power supply instability.',
        'Signal loss detected.',
        'Unauthorized access attempt.',
        'Malfunction in control unit.'
    ]
    error_code = random.choice(error_codes)
    system = random.choice(systems)
    error_message = random.choice(error_messages)
    recommendation = f"Recommendation: {random.choice(['Restart system', 'Run diagnostics', 'Contact engineering team', 'Switch to backup systems', 'Isolate affected components'])}."
    print(f"{color}ERROR {error_code}: {system} System - {error_message}")
    print(f"{color}{recommendation}")


def output_mission_status():
    colors = [Fore.GREEN, Fore.LIGHTBLUE_EX]
    color = random.choice(colors)
    missions = [
        'Exploration of uncharted sector',
        'Rescue mission for stranded vessel',
        'Diplomatic envoy to alien civilization',
        'Scientific research on spatial anomalies',
        'Defense patrol along the neutral zone',
        'Resource extraction operation',
        'First contact protocol with new species',
        'Reconnaissance of enemy territory',
        'Colonization of habitable planet',
        'Time-sensitive medical delivery'
    ]
    mission = random.choice(missions)
    objectives_completed = random.randint(0, 5)
    total_objectives = random.randint(objectives_completed + 1, 5)
    time_remaining = random.randint(1, 72)  # in hours
    success_probability = random.uniform(50, 99.9)
    print(f"{color}Mission Update: {mission}")
    print(f"{color}Objectives Completed: {objectives_completed}/{total_objectives}")
    print(f"{color}Time Remaining: {time_remaining} hours")
    print(f"{color}Success Probability: {success_probability:.2f}%")


def output_data_transfer():
    colors = [Fore.LIGHTCYAN_EX, Fore.LIGHTGREEN_EX]
    color = random.choice(colors)
    files = [
        'Stellar Cartography Data',
        'Quantum Field Reports',
        'Encrypted Command Directives',
        'Medical Research Logs',
        'Alien Language Database',
        'Historical Archives',
        'Engine Performance Metrics',
        'Subspace Communication Logs',
        'Security Clearance Documents',
        'Terraforming Algorithms'
    ]
    file_name = random.choice(files)
    file_size = round(random.uniform(500, 5000), 2)  # in MB
    transfer_rate = round(random.uniform(10, 100), 2)  # in MB/s
    total_time = file_size / transfer_rate
    start_time = time.time()
    elapsed = 0
    print(f"{color}Initiating transfer of '{file_name}' ({file_size} TB)...")
    while elapsed < total_time:
        elapsed = time.time() - start_time
        progress = min(int((elapsed / total_time) * 100), 100)
        bar_length = 50
        filled_length = int(bar_length * progress // 100)
        bar = '█' * filled_length + '-' * (bar_length - filled_length)
        print(f"{color}[{bar}] {progress}% Complete", end='\r')
        time.sleep(0.5)
    print(f"{color}[{'█' * bar_length}] 100% Complete")
    print(f"{color}Transfer of '{file_name}' completed successfully.")


def output_diagnostics():
    colors = [Fore.LIGHTWHITE_EX, Fore.LIGHTBLACK_EX]
    color = random.choice(colors)
    systems = [
        'Life Support', 'Navigation', 'Propulsion', 'Weapons', 'Shields', 'Sensors', 'Communications', 'Artificial Gravity', 'Computer Core', 'Cloaking Device'
    ]
    print(f"{color}Running System Diagnostics...")
    for system in systems:
        status = random.choice(['PASS', 'FAIL'])
        if status == 'PASS':
            status_color = Fore.GREEN
            note = ''
        else:
            status_color = Fore.RED
            note = f" - Issue detected: {random.choice(['Power fluctuation', 'Hardware malfunction', 'Software error', 'Signal interference', 'Overheating'])}"
        print(f"{color}{system}: {status_color}{status}{color}{note}")
        time.sleep(random.uniform(0.2, 0.5))


def output_environmental_readings():
    colors = [Fore.LIGHTGREEN_EX, Fore.LIGHTBLUE_EX]
    color = random.choice(colors)
    readings = [
        ("Radiation Level", f"{random.uniform(0.01, 5.0):.2f} μSv/h"),
        ("External Temperature", f"{random.uniform(-273, 5000):.2f} °C"),
        ("Atmospheric Pressure", f"{random.uniform(0, 101.3):.2f} kPa"),
        ("Gravity Field Strength", f"{random.uniform(0, 20):.2f} m/s²"),
        ("Hull Integrity", f"{random.uniform(75, 100):.2f}%"),
        ("Magnetic Field Flux", f"{random.uniform(0, 500):.2f} μT"),
        ("Solar Wind Speed", f"{random.uniform(300, 800):.2f} km/s"),
        ("Cosmic Ray Intensity", f"{random.uniform(1, 10):.2f} particles/cm²/s"),
        ("Dark Matter Density", f"{random.uniform(0, 0.3):.4f} GeV/cm³"),
        ("Antimatter Containment", f"{random.uniform(90, 100):.2f}%")
    ]
    for name, value in readings:
        warning = ''
        if "Radiation Level" in name and float(value.split()[0]) > 2.0:
            warning = f" {Fore.YELLOW}[High Radiation Alert]"
        elif "Hull Integrity" in name and float(value.strip('%')) < 85.0:
            warning = f" {Fore.RED}[Critical]"
        print(f"{color}{name}: {value}{warning}")
        time.sleep(random.uniform(0.1, 0.3))


def output_progress_bar():
    tasks = [
        'Uploading Data Package',
        'Calibrating Sensors',
        'Processing Quantum Entanglement',
        'Initializing Warp Drive',
        'Analyzing Anomaly',
        'Decrypting Secure Transmission',
        'Compiling Diagnostic Reports',
        'Synchronizing Subspace Frequencies',
        'Establishing Communication Link',
        'Optimizing Power Grid'
    ]

    colors = [
        Fore.GREEN,
        Fore.CYAN,
        Fore.YELLOW,
        Fore.MAGENTA,
        Fore.BLUE,
        Fore.LIGHTGREEN_EX,
        Fore.LIGHTCYAN_EX,
        Fore.LIGHTYELLOW_EX,
        Fore.LIGHTMAGENTA_EX,
        Fore.LIGHTBLUE_EX
    ]

    task = random.choice(tasks)
    color = random.choice(colors)
    total_steps = 50  # Number of steps in the progress bar
    progress = 0
    print(f"{color}{task}...", end='')

    # Variable timing parameters
    min_sleep = 0.05
    max_sleep = 0.2

    while progress <= total_steps:
        percent = int((progress / total_steps) * 100)
        bar_length = 30  # Length of the progress bar display
        filled_length = int(bar_length * progress // total_steps)
        bar = '█' * filled_length + '-' * (bar_length - filled_length)
        print(f"\r{color}{task}... [{bar}] {percent}% Complete", end='')
        time.sleep(random.uniform(min_sleep, max_sleep))
        progress += 1

    # Ensure the line is completed
    print(f"\r{color}{task}... [{'█' * bar_length}] 100% Complete", end='')


def output_formatted_table():
    # Get terminal size
    try:
        terminal_size = os.get_terminal_size()
        terminal_width = terminal_size.columns
    except OSError:
        # Default terminal width if detection fails
        terminal_width = 80

    # Sample data for the table
    headers = ["Parameter", "Value", "Unit"]
    data = [
        ("CPU Usage", f"{random.uniform(0, 100):.2f}", "%"),
        ("Memory Usage", f"{random.uniform(0, 100):.2f}", "%"),
        ("Disk Usage", f"{random.uniform(0, 100):.2f}", "%"),
        ("Network Sent", f"{random.uniform(0, 1024):.2f}", "MB"),
        ("Network Received", f"{random.uniform(0, 1024):.2f}", "MB"),
        ("Active Processes", f"{random.randint(50, 500)}", ""),
        ("System Uptime", f"{random.randint(1, 1000)}", "hours"),
        ("Temperature", f"{random.uniform(20, 90):.2f}", "°C"),
        ("Fan Speed", f"{random.randint(1000, 5000)}", "RPM"),
    ]

    # Calculate column widths
    # Start with the length of the headers
    col_widths = [len(header) for header in headers]

    # Update column widths based on data
    for row in data:
        for i, cell in enumerate(row):
            col_widths[i] = max(col_widths[i], len(str(cell)))

    # Calculate total width needed for the table
    total_table_width = sum(col_widths) + len(col_widths) - 1  # spaces between columns

    # Adjust column widths if total_table_width > terminal_width
    if total_table_width > terminal_width:
        # Calculate the extra width
        extra_width = total_table_width - terminal_width
        # Reduce each column width proportionally
        for i in range(len(col_widths)):
            reduction = int((col_widths[i] / total_table_width) * extra_width)
            col_widths[i] -= reduction
        # Recalculate total_table_width
        total_table_width = sum(col_widths) + len(col_widths) - 1

    # Prepare format string
    format_str = ""
    for i in range(len(col_widths)):
        format_str += f"{{:<{col_widths[i]}}}"
        if i < len(col_widths) - 1:
            format_str += " "

    # Print the table
    color = Fore.LIGHTWHITE_EX
    # Print header
    header_line = format_str.format(*headers)
    print(color + header_line, end="")
    # Print separator line
    print(color + "\n" + "-" * total_table_width, end="")
    # Print data rows
    for row in data:
        line = format_str.format(*row)
        print(color + "\n" + line, end="")


def main():
    functions = [output_data_point, output_long_text, output_table, output_random_event, output_encrypted_transmission, output_decryption_attempt,
                 output_star_map_coordinates, output_algorithm_processing, output_anomaly_detection, output_ai_dialogue, output_system_errors,
                 output_mission_status, output_data_transfer, output_diagnostics, output_environmental_readings, output_formatted_table,
                 output_progress_bar]
    try:
        while True:
            func = random.choice(functions)
            func()
            time.sleep(random.uniform(0.5, 5.5))
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")

if __name__ == "__main__":
    main()
