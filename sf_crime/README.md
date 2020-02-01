#How did changing values on the SparkSession property parameters affect the throughput and latency of the data?

Yes, some differences could be verified when using extremely large values for maxOffsetsPerTrigger.

#What were the 2-3 most efficient SparkSession property key/value pairs? Through testing multiple variations on values, how can you tell these were the most optimal?

One of the most notable config was the maxOffsetsPerTrigger, since it will determine how many messages each trigger event will wait. For configurations with streaming in which a processingTime trigger is often used, whis could be problematic. 

The next configuration used was maxRatePerPartition, which determines max messages per partition per topic.

I did not test extensively, but results were ok for the selected values. Also, I set the rate of producer to 1 message per second for only one partition, so it is not an overwhelming load that could result in performance problems.