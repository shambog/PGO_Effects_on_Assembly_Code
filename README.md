# PGO_Effects_on_Assembly_Code
## A study on the effects of PGO using Hotspot VM


## Authors
* Naveed Mahmud
* Shambo Ghosh



## Profile Guided Optimization (PGO)

Profile-guided optimizations (PGO) in a JVM employs profiling to understand execution-time program behavior and exploit that information to generate higher-quality code during code generation. We are studying the ratio of methods that are affected by PGOs by comparing generated object codes directly.

## Results

We created the follwing Java programs an compiled them with Hotspot VM with PGO turned ON and OFF. In both of these cases we generated assembly code and compared them using our Python script. We got the following results from our experiments. <br/>

![Table](https://user-images.githubusercontent.com/35944630/57963099-24b20080-78e5-11e9-9f86-980d51393fd3.PNG)


## Project Structure
 
 **parse_logs_v3.py** - This script parses the assembly code<br/>
 **exception_out.log** - Log file for the exception java program<br/>
 **factorial_out.log** - Log file for the factorial java program<br/>
 **helloworld_out.log** - Log file for the helloworld java program<br/>
 **transpose_out.log** - Log file for the transpose java program<br/>

## References

1. https://www.ibm.com/developerworks/library/j-jtp12214/
2. https://blog.overops.com/java-on-steroids-5-super-useful-jit-optimization-techniques/
3. https://www.oracle.com/technetwork/java/javase/tech/vmoptions-jsp-140102.html



