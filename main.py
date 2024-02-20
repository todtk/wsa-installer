import win32com.client
import psutil


def check_os_version() -> bool:
    """
    Операционная система: Windows 11 серии 22000.xxx и выше
    """
    pass


def check_ram() -> bool:
    """Проверяет соответствие трабованиям RAM (>16GB)"""
    return (psutil.virtual_memory().total / 1000000000) > 17


def check_architecture() -> bool:
    """
    Архитектура процессора: x64 или ARM64
    """


def check_virtualization() -> bool:
    """
    Включена виртуализация в BIOS/UEFI
    """
    wmi = win32com.client.GetObject("winmgmts:")
    for cpu in wmi.InstancesOf('Win32_Processor'):
        return cpu.VirtualizationFirmwareEnabled


def check_virtual_machine() -> bool:
    """
    Активированная настройка «Платформа виртуальной машины»
    """
    pass


print(check_ram())