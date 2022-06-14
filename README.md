# CMP2204 Introduction to Computer Networks

## Spring 2021, Term Project

## Project Report

Task: A simple command line application for data sharing over local network.

Group Members: Kaan Sevenler 1903253
Melisa Çevik 1903028

Platform we have used to develop our code: Windows 10

IDE we used to develop our code: Pycharm IDE

## Faced challenges and limitations :

- To host more than one file from one host, chunk announcer must be run once for each
    file.
- If file host user deletes a chunk file it will not be recreated nor will the downloader be
    aware of it (the download will simply fail stating the deleted chunk could not be
    downloaded from any known sources)
- In Chunk Downloader, if there has been a problem downloading any of the chunks and
    program did not read any bytes, it still created a file of 0 kb. We fixed it by reading the
    bytes in if statement and if there isn’t any bytes have been read we raised an IOError
    (lines 48-60)
- At the beginning our program used same port for both UDP processes so it caused one
    of the programs to shout down. We made Chunk Announcer and Chunk Downloader
    choose from the available ports to get around the problem.

## Division of Workload

## Kaan Sevenler Melisa Çevik

```
Chunk Downloader Chunk Announcement
Chunk Uploader Content Discovery
Solutions for faced challenges Read Me and Project Report
```

