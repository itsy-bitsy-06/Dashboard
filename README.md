# Dashboard Documentation

# Introduction

This repository contains the content for the Dashboard project.

The Dashboard project provides a platform to remotely manage Mini_ULT (User-Level Test) application on any card that can be represented as a logical drive within the Windows operating system.

Currently, most 32-bit and 64-bit Windows operating systems are supported. The project is currently in development.

# Windows Setup
Windows automatic updates have to be enabled to upgrade powershell, to do that:
`Control panel -> Windows update  (is disabled) ->System and Security ->Windows Update >Change settings ->Automatic

## Network adapter settings check
Network profile needs to be changed to Private / Work for all interfaces.

## Windows 7
Windows 7 has the default power shell version 2.x
To upgrade it:
    - Install dotnet runtime > version 4.5
    - Install powershell > version 3.0

## Check PowerShell execution policies
Launch powershell prompt as administrator and run following policies

`Get-ExecutionPolicy`

If this is restricted then run

`Set-ExecutionPolicy -ExecutionPolicy Unrestricted`

## Commands powershell list drives

`Get-WmiObject Win32_LogicalDisk -filter "DriveType='2'" | ft DeviceID,FileSystem,FreeSpace,Size`
