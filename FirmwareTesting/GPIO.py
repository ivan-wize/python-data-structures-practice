# Here are a few Python code examples that could be used to test the bringup of
#  FPGA and SoC silicon hardware. These scripts typically interact with hardware
# using libraries like pyserial, RPi.GPIO (for Raspberry Pi GPIO testing), or custom
# APIs provided by the hardware vendor. I'll demonstrate a few scenarios:

import RPi.GPIO as GPIO
import serial
import spidev
import time

# ==============================================
# 1. GPIO Test for FPGA or SoC
# ==============================================
def gpio_test():
    """
    Toggles a GPIO pin and reads the input pin to verify functionality.
    """
    PIN_OUT = 17  # Output pin
    PIN_IN = 27   # Input pin

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(PIN_OUT, GPIO.OUT)
    GPIO.setup(PIN_IN, GPIO.IN)

    print("Starting GPIO Test...")
    try:
        for i in range(5):  # Toggle 5 times
            GPIO.output(PIN_OUT, GPIO.HIGH)
            time.sleep(0.5)
            state = GPIO.input(PIN_IN)
            print(f"Cycle {i + 1}: Read state = {state}")
            GPIO.output(PIN_OUT, GPIO.LOW)
            time.sleep(0.5)
    except Exception as e:
        print(f"Error during GPIO test: {e}")
    finally:
        GPIO.cleanup()
        print("GPIO Test Complete.")

# ==============================================
# 2. UART Communication Test
# ==============================================
def uart_test(port='/dev/ttyUSB0', baudrate=115200):
    """
    Sends and receives data over UART to validate communication.
    """
    try:
        ser = serial.Serial(port, baudrate, timeout=1)
        print(f"Connected to {port} at {baudrate} baud.")

        # Test write
        message = "Hello FPGA!"
        ser.write(message.encode('utf-8'))
        print(f"Sent: {message}")

        # Test read
        response = ser.readline().decode('utf-8').strip()
        print(f"Received: {response}")

        if response == message:
            print("UART loopback test passed!")
        else:
            print("UART loopback test failed.")
    except Exception as e:
        print(f"Error during UART test: {e}")
    finally:
        ser.close()

# ==============================================
# 3. SPI Communication Test
# ==============================================
def spi_test(bus=0, device=0):
    """
    Sends and receives data over SPI to validate communication.
    """
    try:
        spi = spidev.SpiDev()
        spi.open(bus, device)
        spi.max_speed_hz = 500000  # 500 kHz

        # Test write and read
        test_data = [0x01, 0x02, 0x03, 0x04]
        print(f"Sending: {test_data}")
        response = spi.xfer2(test_data)
        print(f"Received: {response}")

        if response == test_data:
            print("SPI loopback test passed!")
        else:
            print("SPI loopback test failed.")
    except Exception as e:
        print(f"Error during SPI test: {e}")
    finally:
        spi.close()

# ==============================================
# Main Function to Run All Tests
# ==============================================
if __name__ == "__main__":
    print("Starting FPGA/SoC Hardware Tests...")

    print("\nRunning GPIO Test...")
    gpio_test()

    print("\nRunning UART Test...")
    uart_test()

    print("\nRunning SPI Test...")
    spi_test()

    print("\nAll tests completed.")
