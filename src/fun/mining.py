import wmi

'''

хи-хи ха-ха, шутка
he-he ha-ha is a joke

'''

computer = wmi.WMI()
os_info = computer.Win32_OperatingSystem()[0]

proc_info = computer.Win32_Processor()[0]
gpu_info = computer.Win32_VideoController()[0]
os_version = ' '.join([os_info.Version, os_info.BuildNumber])
system_ram = float(os_info.TotalVisibleMemorySize) // 1048576  # KB to GB


def mining_start():
    print('BTC-Mining has alredy working!\nBTC-Wallet: q5sh1ujajk009172lna173kmbnyq92163kpa\n\n')
    print('MINING SYSTEM:\n')
    print('OS Version: {0}'.format(os_version))
    print('CPU: {0}'.format(proc_info.Name))
    print('Graphics Card: {0}'.format(gpu_info.Name))
    print('RAM: {0} GB'.format(system_ram))
    print('\n\n\nBTC-amount: ~0,000481 btc per hour\n\n')
    print('Mining...')
