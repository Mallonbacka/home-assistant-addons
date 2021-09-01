# Backup Cleaner

## How it works

There's a tiny shell script which takes care of the delay between calls to the Python script.

The Python script is quite self-explanatory, but in short it  grabs a list of all full backups, then picks out the latest before finally deleting any others.

After the script has run, the shell script takes care of sleeping the number of seconds listed in `delay` before trying the script again.

Backup Cleaner ignores partial backups.

## Configuration

### Delay (required)

The number of seconds to wait between checks. Defaults to `10800` (three hours), but `86400` (24 hours) is a good option too.
