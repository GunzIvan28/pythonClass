Based on the time from start to the first two cracks, the threaded cracker seems to be about 1/3 - 2/3 the speed of the recursive cracker (the gap maybe widening or lessening exponentially). It's possible that the reason for this is that the start time is output to a file followed by thread creation. Whereas in the recursive cracker, the start time is ouput to a file followed by immediate hash creation/comparison. Creating the threads might be causing the slightest bit of overhead and prolonging the time-to-crack. 

That's only speculation though. I honeslty have no idea as to the actual reason for the difference and can only speculate.

Below are the times for each cracker for the first two hashes.

****THREADED CRACKER OUTPUT****

Begin: Tue Apr 23 13:02:28 2013

Password found: Tue Apr 23 13:02:39 2013
Hash2 = your
Password found: Tue Apr 23 13:03:06 2013
Hash1 = drink


****RECURSIVE CRACKER OUTPUT****

Starting at: Tue Apr 23 13:01:35 2013

Hash: 62cc0b4ebb0b57b40778179234246c38
Password: your
Time of crack: Tue Apr 23 13:01:39 2013

Hash: 0b18a3d7b9c43ff1750d2baa4606b8d0
Password: drink
Time of crack: Tue Apr 23 13:01:57 2013