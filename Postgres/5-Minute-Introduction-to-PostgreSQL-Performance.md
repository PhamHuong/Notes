5-Minute Introduction to PostgreSQL Performance
=================================================
PostgreSQL ships with a basic configuration tuned for wide compatibility rather than performance. Odds are good the default parameters are very undersized for your system. Rather than get dragged into the details of everything you should eventually know, here we're going to sprint through a simplified view of the basics, with a look at the most common performance-related things people new to PostgreSQL aren't aware of. For a really quick read, just skim the bolded lines in each section and follow those guidelines.
The main database server parameters are held in a file named postgresql.conf. You will need to edit this file and restart your server for changes to be effective. Note that performance may actually drop for a short period after doing this, because you'll lose information that is cached in memory in the restart.

*Use a current version*

The earliest version of PostgreSQL that has good performance on current hardware is 8.1; the current 8.2 is even better (and you should be running 8.2.4, earlier 8.2 releases had some quirks you're better off avoiding). If you're running an earlier PostgreSQL version than 8.1, you should upgrade. There are many performance issues you can run into that are unresolvable with earlier versions. The guidelines of the next section aren't appropriate if you're running an old release.
Set shared_buffers and effective_cache_size based on total memory

The shared_buffers configuration parameter determines how much memory is dedicated to PostgreSQL use for caching data. A reasonable starting value for shared_buffers is 1/4 of the memory in your system. It's likely you will have to increase the amount of memory your operating system allows you to allocate at once to set the value this high; see Managing Kernel Resources for details. Note that on Windows, large values for shared_buffers aren't as effective, and you may find better results keeping it relatively low and using the OS cache more instead.
effective_cache_size should be set to how much memory is leftover for disk caching after taking into account what's used by the operating system, dedicated PostgreSQL memory, and other applications. If it's set too low, indexes may not be used for executing queries the way you'd expect. Setting effective_cache_size to 1/2 of total memory would be a normal conservative setting. You might find a better estimate by looking at your operating system's statistics. On UNIX-like systems, add the free+cached numbers from free or top. On Windows see the "System Cache" in the Windows Task Manager's Performance tab. Note that you should add whatever value you set to shared_buffers to this total--the query planner uses estimated_cache_size as-is, without also adding that value for you.

*ANALYZE your database*

PostgreSQL keeps statistics about your database tables that allow it to correctly execute queries. If these statistics are out of date, you will not get good performance. You can update the stats using the ANALYZE command. To do that and clean out unused data, execute the VACCUM ANALYZE command in order to force a statistics update and table cleanup. This is particularly important if you've just loaded or modified a large amount of data. You should look into automatically vacuuming your tables if you're not already, which will also keep the statistics current.
EXPLAIN ANALYZE your slow statements

If you have a specific statement you're executing that is taking longer than expected, the best way to figure out why it's not running faster to look at what it's doing. Run EXPLAIN ANALYZE to get a report of why a statement is taking a long time to execute. This may lead you to adjusting other server parameters; for example, if you notice that a sort operation is taking a long time, you might need to increase the work_mem parameter in your postgresql.conf. Note that work_mem is set on a per-client connection basis, so you need to multiply the value by the concurrent sessions to get a total memory figure. You can use increase the value just for one session that runs a larger query than most by using a command like set work_mem = '1GB'; (that's the 8.2 syntax; you'll have to manually specify a value in 8.1 instead).
