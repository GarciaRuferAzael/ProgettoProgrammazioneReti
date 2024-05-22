#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 20 17:30:51 2024

@author: azaelgarciarufer
"""
import platform
import subprocess
import ipaddress

def ping_host(ip):
    
    #param of command: '-n' if OS is Windows, '-c' if OS is macOs or Linux
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    command = ["ping", param, "1", ip]
    
    #running command ping and return True if host is reachable, False if not.
    try:
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=15)
        return result.returncode == 0
    except Exception as e:
        print(f"Error during the ping of {ip}: {str(e)}")
        return False


def monitor_hosts():
    
    #request input (separated by white space)
    ips = input("Insert IP addresses to check their status (separated by white space): ").split()
    
    #input exceptions.
    if not ips:
        print("No IP addresses provided.")
        return
    
    #check if IP is valid.
    for ip in ips:
        try:
            ipaddress.ip_address(ip)
        except ValueError:
            print(f"{ip} is not valid")
            continue
        
        #print status.
        try:
            if ping_host(ip):
                print(f"{ip} is online")
            else:
                print(f"{ip} is offline")
        except subprocess.TimeoutExpired:
            print(f"{ip} failed to check (timeout)")
            continue

if __name__ == "__main__":
    monitor_hosts()

