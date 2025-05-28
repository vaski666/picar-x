from time import sleep
import random
from math import sin, cos, pi
from keyboard_control import manual_drive as drive_action

# Legg til import for kamera
import os
import base64
from picamera2 import Picamera2 # Importer Picamera2
# Du trenger ikke OpenAI imports her hvis du kaller APIet et annet sted
# from openai import OpenAI
# from dotenv import load_dotenv

# Fjern OpenAI klient initialisering herfra hvis du flytter API-kallet

def wave_hands(car):
    car.reset()
    car.set_cam_tilt_angle(20)
    for _ in range(2):
        car.set_dir_servo_angle(-25)
        sleep(.1)
        car.set_dir_servo_angle(25)
        sleep(.1)
    car.set_dir_servo_angle(0)

def resist(car):
    car.reset()
    car.set_cam_tilt_angle(10)
    for _ in range(3):
        car.set_dir_servo_angle(-15)
        car.set_cam_pan_angle(15)
        sleep(.1)
        car.set_dir_servo_angle(15)
        car.set_cam_pan_angle(-15)
        sleep(.1)
    car.stop()
    car.set_dir_servo_angle(0)
    car.set_cam_pan_angle(0)

def act_cute(car):
    car.reset()
    car.set_cam_tilt_angle(-20)
    for i in range(15):
        car.forward(5)
        sleep(0.02)
        car.backward(5)
        sleep(0.02)
    car.set_cam_tilt_angle(0)
    car.stop()

def rub_hands(car):
    car.reset()
    for i in range(5):
        car.set_dir_servo_angle(-6)
        sleep(.5)
        car.set_dir_servo_angle(6)
        sleep(.5)
    car.reset()

def think(car):
    car.reset()

    for i in range(11):
        car.set_cam_pan_angle(i*3)
        car.set_cam_tilt_angle(-i*2)
        car.set_dir_servo_angle(i*2)
        sleep(.05)
    sleep(1)
    car.set_cam_pan_angle(15)
    car.set_cam_tilt_angle(-10)
    car.set_dir_servo_angle(10)
    sleep(.1)
    car.reset()

def keep_think(car):
    car.reset()
    for i in range(11):
        car.set_cam_pan_angle(i*3)
        car.set_cam_tilt_angle(-i*2)
        car.set_dir_servo_angle(i*2)
        sleep(.05)

def shake_head(car):
    car.stop()
    car.set_cam_pan_angle(0)
    car.set_cam_pan_angle(60)
    sleep(.2)
    car.set_cam_pan_angle(-50)
    sleep(.1)
    car.set_cam_pan_angle(40)
    sleep(.1)
    car.set_cam_pan_angle(-30)
    sleep(.1)
    car.set_cam_pan_angle(20)
    sleep(.1)
    car.set_cam_pan_angle(-10)
    sleep(.1)
    car.set_cam_pan_angle(10)
    sleep(.1)
    car.set_cam_pan_angle(-5)
    sleep(.1)
    car.set_cam_pan_angle(0)

def nod(car):
    car.reset()
    car.set_cam_tilt_angle(0)
    car.set_cam_tilt_angle(5)
    sleep(.1)
    car.set_cam_tilt_angle(-30)
    sleep(.1)
    car.set_cam_tilt_angle(5)
    sleep(.1)
    car.set_cam_tilt_angle(-30)
    sleep(.1)
    car.set_cam_tilt_angle(0)


def depressed(car):
    car.reset()
    car.set_cam_tilt_angle(0)
    car.set_cam_tilt_angle(20)
    sleep(.22)
    car.set_cam_tilt_angle(-22)
    sleep(.1)
    car.set_cam_tilt_angle(10)
    sleep(.1)
    car.set_cam_tilt_angle(-22)
    sleep(.1)
    car.set_cam_tilt_angle(0)
    sleep(.1)
    car.set_cam_tilt_angle(-22)
    sleep(.1)
    car.set_cam_tilt_angle(-10)
    sleep(.1)
    car.set_cam_tilt_angle(-22)
    sleep(.1)
    car.set_cam_tilt_angle(-15)
    sleep(.1)
    car.set_cam_tilt_angle(-22)
    sleep(.1)
    car.set_cam_tilt_angle(-19)
    sleep(.1)
    car.set_cam_tilt_angle(-22)
    sleep(.1)

    sleep(1.5)
    car.reset()

def twist_body(car):
    car.reset()
    for i in range(3):
        car.set_motor_speed(1, 20)
        car.set_motor_speed(2, 20)
        car.set_cam_pan_angle(-20)
        car.set_dir_servo_angle(-10)
        sleep(.1)
        car.set_motor_speed(1, 0)
        car.set_motor_speed(2, 0)
        car.set_cam_pan_angle(0)
        car.set_dir_servo_angle(0)
        sleep(.1)
        car.set_motor_speed(1, -20)
        car.set_motor_speed(2, -20)
        car.set_cam_pan_angle(20)
        car.set_dir_servo_angle(10)
        sleep(.1)
        car.set_motor_speed(1, 0)
        car.set_motor_speed(2, 0)
        car.set_cam_pan_angle(0)
        car.set_dir_servo_angle(0)
        sleep(.1)

def forward_one_second(car):
    car.reset()
    car.set_motor_speed(1, 20)
    car.set_motor_speed(2, 20)
    sleep(1)
    car.stop()

def backward_one_second(car):
    car.reset()
    car.set_motor_speed(1, -20)
    car.set_motor_speed(2, -20)
    sleep(1)
    car.stop()

def turn_right(car):
    car.reset()
    car.set_dir_servo_angle(30)
    car.set_motor_speed(1, 20)
    car.set_motor_speed(2, 20)
    sleep(1)
    car.stop()
    car.set_dir_servo_angle(0)

def turn_left(car):
    car.reset()
    car.set_dir_servo_angle(-30)
    car.set_motor_speed(1, 20)
    car.set_motor_speed(2, 20)
    sleep(1)
    car.stop()
    car.set_dir_servo_angle(0)

def honking(music):
    import utils
    music.sound_play_threading("../sounds/car-double-horn.wav", 100)

def start_engine(music):
    import utils
    music.sound_play_threading("../sounds/car-start-engine.wav", 50)

# Funksjon for å ta bilde og returnere base64-data
def take_picture(car):
    print("Taking picture...")
    file_path = "/tmp/picarx_image.jpg" # Midlertidig filsti
    base64_image = None
    
    try:
        picam2 = Picamera2()
        camera_config = picam2.create_still_configuration(main={"size": (1280, 720)})
        picam2.configure(camera_config)
        picam2.start()
        sleep(2) # Gi kameraet tid til å justere seg
        picam2.capture_file(file_path)
        picam2.stop()
        print(f"Picture saved to {file_path}")

        # Les bildet og konverter til Base64
        def encode_image(image_path):
            with open(image_path, "rb") as image_file:
                return base64.b64encode(image_file.read()).decode('utf-8')

        base64_image = encode_image(file_path)
        print("Image encoded to Base64.")

    except FileNotFoundError:
        print(f"Error: Camera module not found or unable to save image to {file_path}. Make sure the camera is connected and enabled.")
    except Exception as e:
        print(f"An error occurred during image capture: {e}")
    finally:
        # Rydd opp den midlertidige bildefilen
        if os.path.exists(file_path):
            os.remove(file_path)
        car.reset() # Sørg for at roboten er i en nøytral tilstand
        return base64_image # Returner Base64-dataen

actions_dict = {
    "shake head":shake_head,
    "nod": nod,
    "wave hands": wave_hands,
    "resist": resist,
    "act cute": act_cute,
    "rub hands": rub_hands,
    "think": think,
    "twist body": twist_body,
    "celebrate": celebrate,
    "depressed": depressed,
    "drive": drive_action,
    "forward one second": forward_one_second,
    "backward one second": backward_one_second,
    "turn right": turn_right,
    "turn left": turn_left,
    "take picture": take_picture, # Legg til den nye bevegelsen
}

sounds_dict = {
    "honking": honking,
    "start engine": start_engine,
}


if __name__ == "__main__":
    from picarx import Picarx
    from robot_hat import Music
    import os
    from openai import OpenAI # Import OpenAI here if you want to use it in main
    from dotenv import load_dotenv # Import load_dotenv here if you want to use it in main

    # Last API-nøkkelen her hvis du skal kalle OpenAI fra main
    load_dotenv()
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    client = OpenAI(api_key=OPENAI_API_KEY)


    os.popen("pinctrl set 20 op dh") # enable robot_hat speake switch
    current_path = os.path.dirname(os.path.abspath(__file__))
    os.chdir(current_path) # change working directory

    my_car = Picarx()
    my_car.reset()

    music = Music()

    sleep(.5)

    _actions_num = len(actions_dict)
    actions = list(actions_dict.keys())
    for i, key in enumerate(actions_dict):
        print(f'{i} {key}')

    _sounds_num = len(sounds_dict)
    sounds = list(sounds_dict.keys())
    for i, key in enumerate(sounds_dict):
        print(f'{_actions_num+i} {key}')

    last_key = None

    try:
        while True:
            key = input()

            if key == '':
                if last_key is not None:
                    if last_key > _actions_num - 1:
                        print(sounds[last_key-_actions_num])
                        sounds_dict[sounds[last_key-_actions_num]](music)
                    else:
                        selected_action_name = actions[last_key]
                        print(selected_action_name)
                        if selected_action_name == "take picture":
                            # Kall take_picture og send deretter til OpenAI
                            base64_image = actions_dict[selected_action_name](my_car)
                            if base64_image:
                                print("Sending image to OpenAI for analysis...")
                                try:
                                    response = client.chat.completions.create(
                                        model="gpt-4o-mini", # Eller "gpt-4-vision-preview"
                                        messages=[
                                            {
                                                "role": "user",
                                                "content": [
                                                    {"type": "text", "text": "Describe this image and identify any objects or features relevant to robot car navigation (e.g., road, obstacles, turns, traffic signs). Based on the image, what action should the robot take next (e.g., 'go forward', 'turn left', 'turn right', 'stop')?"},
                                                    {
                                                        "type": "image_url",
                                                        "image_url": {
                                                            "url": f"data:image/jpeg;base64,{base64_image}",
                                                            "detail": "low"
                                                        }
                                                    }
                                                ]
                                            }
                                        ],
                                        max_tokens=300,
                                    )
                                    analysis_result = response.choices[0].message.content
                                    print("OpenAI Analysis:")
                                    print(analysis_result)

                                    # Her kan du legge til logikk for å tolke analysen og kalle neste handling
                                    # For eksempel:
                                    # if "go forward" in analysis_result.lower():
                                    #     forward_one_second(my_car)
                                    # elif "turn left" in analysis_result.lower():
                                    #     turn_left(my_car)
                                    # elif "turn right" in analysis_result.lower():
                                    #     turn_right(my_car)
                                    # else:
                                    #     my_car.stop()

                                except Exception as api_e:
                                    print(f"Error during OpenAI API call: {api_e}")
                            else:
                                print("No image data received for analysis.")
                        else:
                            actions_dict[selected_action_name](my_car)
                else:
                    print("No previous action to repeat. Please enter a number.")
            else:
                try:
                    key = int(key)
                    if key > (_actions_num + _sounds_num - 1) or key < 0:
                        print("Invalid key")
                    elif key > (_actions_num - 1):
                        last_key = key
                        print(sounds[last_key-_actions_num])
                        sounds_dict[sounds[last_key-_actions_num]](music)
                    else:
                        last_key = key
                        selected_action_name = actions[key]
                        print(selected_action_name)
                        if selected_action_name == "take picture":
                            base64_image = actions_dict[selected_action_name](my_car)
                            if base64_image:
                                print("Sending image to OpenAI for analysis...")
                                try:
                                    response = client.chat.completions.create(
                                        model="gpt-4o-mini", # Eller "gpt-4-vision-preview"
                                        messages=[
                                            {
                                                "role": "user",
                                                "content": [
                                                    {"type": "text", "text": "Describe this image and identify any objects or features relevant to robot car navigation (e.g., road, obstacles, turns, traffic signs). Based on the image, what action should the robot take next (e.g., 'go forward', 'turn left', 'turn right', 'stop')?"},
                                                    {
                                                        "type": "image_url",
                                                        "image_url": {
                                                            "url": f"data:image/jpeg;base64,{base64_image}",
                                                            "detail": "low"
                                                        }
                                                    }
                                                ]
                                            }
                                        ],
                                        max_tokens=300,
                                    )
                                    analysis_result = response.choices[0].message.content
                                    print("OpenAI Analysis:")
                                    print(analysis_result)

                                    # Her kan du legge til logikk for å tolke analysen og kalle neste handling
                                    # if "go forward" in analysis_result.lower():
                                    #     forward_one_second(my_car)
                                    # elif "turn left" in analysis_result.lower():
                                    #     turn_left(my_car)
                                    # elif "turn right" in analysis_result.lower():
                                    #     turn_right(my_car)
                                    # else:
                                    #     my_car.stop()

                                except Exception as api_e:
                                    print(f"Error during OpenAI API call: {api_e}")
                            else:
                                print("No image data received for analysis.")
                        else:
                            actions_dict[selected_action_name](my_car)
                except ValueError:
                    print("Invalid input. Please enter a number or press Enter to repeat last action.")

    except KeyboardInterrupt:
        pass
    except Exception as e:
        print(f'Error:\n {e}')
    finally:
        my_car.reset()
        sleep(.1)
