# 深度解读：Performance Testing（性能测试）

> 原文：[Performance Testing](https://microsoft.github.io/code-with-engineering-playbook/automated-testing/performance-testing/)<br>
> 作者：Microsoft ISE（Industry Solutions Engineering，微软行业解决方案工程团队）<br>
> 日期：2026-08-19 17:45

## 原文及译文

<details>
<summary>原文</summary>
<section>

# Performance Testing

**Source:** [Microsoft Engineering Fundamentals Playbook — Performance Testing](https://github.com/microsoft/code-with-engineering-playbook) (open source, MIT-licensed)
**Organization:** Microsoft ISE Engineering Fundamentals Playbook
**Last updated:** August 22, 2024

---

Performance Testing is an overloaded term that is used to refer to several subcategories of performance related testing, each of which has different purpose.

A good description of overall performance testing is as follows:

> "Performance testing is a type of testing intended to determine the responsiveness, throughput, reliability, and/or scalability of a system under a given workload." — [Performance Testing Guidance for Web Applications](https://learn.microsoft.com/en-us/archive/blogs/dajung/ebook-pnp-performance-testing-guidance-for-web-applications)

## Why Performance Testing

Performance testing is commonly conducted to accomplish one or more the following:

- **Tune the system's performance**
  - Identifying bottlenecks and issues with the system at different load levels.
  - Comparing performance characteristics of the system for different system configurations.
  - Come up with a scaling strategy for the system.
- Assist in **capacity planning**
  - Capacity planning is the process of determining what type of hardware and software resources are required to run an application to support pre-defined performance goals.
  - Capacity planning involves identifying business expectations, the periodic fluctuations of application usage, considering the cost of running the hardware and software infrastructure.
- Assess the **system's readiness** for release:
  - Evaluating the system's performance characteristics (response time, throughput) in a production-like environment. The goal is to ensure that performance goals can be achieved upon release.
- Evaluate the **performance impact of application changes**
  - Comparing the performance characteristics of an application after a change to the values of performance characteristics during previous runs (or baseline values), can provide an indication of performance issues (performance regression) or enhancements introduced due to a change.

## Key Performance Testing Categories

Performance testing is a broad topic. There are many areas where you can perform tests. In broad strokes you can perform tests on the backend and on the front end. You can test the performance of individual components as well as testing the end-to-end functionality.

There are several categories of tests as well:

### Load Testing

This is the subcategory of performance testing that focuses on validating the performance characteristics of a system, when the system faces the load volumes which are expected during production operation. An **Endurance Test** or a **Soak Test** is a load test carried over a long duration ranging from several hours to days.

### Stress Testing

This is the subcategory of performance testing that focuses on validating the performance characteristics of a system when the system faces extreme load. The goal is to evaluate how does the system handles being pressured to its limits, does it recover (i.e., scale-out) or does it just break and fail?

### Endurance Testing

The goal of endurance testing is to make sure that the system can maintain good performance under extended periods of load.

### Spike Testing

The goal of Spike testing is to validate that a software system can respond well to large and sudden spikes.

### Chaos Testing

Chaos testing or Chaos engineering is the practice of experimenting on a system to build confidence that the system can withstand turbulent conditions in production. Its goal is to identify weaknesses before they manifest system wide. Developers often implement fallback procedures for service failure. Chaos testing arbitrarily shuts down different parts of the system to validate that fallback procedures function correctly.

## Best Practices

Consider the following best practices for performance testing:

- **Make one change at a time.** Don't make multiple changes to the system between tests. If you do, you won't know which change caused the performance to improve or degrade.
- **Automate testing.** Strive to automate the setup and teardown of resources for a performance run as much as possible. Manual execution can lead to misconfigurations.
- **Use different IP addresses.** Some systems will throttle requests from a single IP address. If you are testing a system that has this type of restriction, you can use different IP addresses to simulate multiple users.

## Performance Monitor Metrics

When executing the various types of testing approaches, whether it is stress, endurance, spike, or chaos testing, it is important to capture various metrics to see how the system performs.

At the basic hardware level, there are four areas to consider:

- Physical disk
- Memory
- Processor
- Network

These four areas are inextricably linked, meaning that poor performance in one area will lead to poor performance in another area. Engineers concerned with understanding application performance, should focus on these four core areas.

The classic example of how performance in one area can affect performance in another area is memory pressure. If an application's available memory is running low, the operating system will try to compensate for shortages in memory by transferring pages of data from memory to disk, thus freeing up memory. But this work requires help from the CPU and the physical disk. This means that when you look at performance when there are low amounts of memory, you will also notice spikes in disk activity as well as CPU.

### Physical Disk

Almost all software systems are dependent on the performance of the physical disk. This is especially true for the performance of databases. More modern approaches to using SSDs for physical disk storage can dramatically improve the performance of applications. Here are some of the metrics that you can capture and analyze:

| Counter | Description |
|---|---|
| Avg. Disk Queue Length | This value is derived using the (Disk Transfers/sec)\*(Disk sec/Transfer) counters. This metric describes the disk queue over time, smoothing out any quick spikes. Having any physical disk with an average queue length over 2 for prolonged periods of time can be an indication that your disk is a bottleneck. |
| % Idle Time | This is a measure of the percentage of time that the disk was idle. ie. there are no pending disk requests from the operating system waiting to be completed. A low number here is a positive sign that disk has excess capacity to service or write requests from the operating system. |
| Avg. Disk sec/Read and Avg. Disk sec/Write | These both measure the latency of your disks. Latency is defined as the average time it takes for a disk transfer to complete. You obviously want is low numbers as possible but need to be careful to account for inherent speed differences between SSD and traditional spinning disks. For this counter is important to define a baseline after the hardware is installed. Then use this value going forward to determine if you are experiencing any latency issues related to the hardware. |
| Disk Reads/sec and Disk Writes/sec | These counters each measure the total number of IO requests completed per second. Similar to the latency counters, good and bad values for these counters depend on your disk hardware but values higher than your initial baseline don't normally point to a hardware issue in this case. This counter can be useful to identify spikes in disk I/O. |

### Processor

It is important to understand the amount of time spent in kernel or privileged mode. In general, if code is spending too much time executing operating system calls, that could be an area of concern because it will not allow you to run your user mode applications, such as your databases, Web servers/services, etc.

The guideline is that the CPU should only spend about 20% of the total processor time running in kernel mode.

| Counter | Description |
|---|---|
| % Processor time | This is the percentage of total elapsed time that the processor was busy executing. This counter can either be too high or too low. If your processor time is consistently below 40%, then there is a question as to whether you have over provisioned your CPU. 70% is generally considered a good target number and if you start going higher than 70%, you may want to explore why there is high CPU pressure. |
| % Privileged (Kernel Mode) time | This measures the percentage of elapsed time the processor spent executing in kernel mode. Since this counter takes into account only kernel operations a high percentage of privileged time (greater than 25%) may indicate driver or hardware issue that should be investigated. |
| % User time | The percentage of elapsed time the processor spent executing in user mode (your application code). A good guideline is to be consistently below 65% as you want to have some buffer for both the kernel operations mentioned above as well as any other bursts of CPU required by other applications. |
| Queue Length | This is the number of threads that are ready to execute but waiting for a core to become available. On single core machines a sustained value greater than 2-3 can mean that you have some CPU pressure. Similarly, for a multicore machine divide the queue length by the number of cores and if that is continuously greater than 2-3 there might be CPU pressure. |

### Network Adapter

Network speed is often a hidden culprit of poor performance. Finding the root cause to poor network performance is often difficult. The source of issues can originate from bandwidth hogs such as videoconferencing, transaction data, network backups, recreational videos.

In fact, the three most common reasons for a network slow down are:

- Congestion
- Data corruption
- Collisions

Some of the tools that can help include:

- ifconfig
- netstat
- iperf
- tcpretrans
- tcpdump
- WireShark

Troubleshooting network performance usually begins with checking the hardware. Typical things to explore is whether there are any loose wires or checking that all routers are powered up. It is not always possible to do so, but sometimes a simple case of power recycling of the modem or router can solve many problems.

Network specialists often perform the following sequence of troubleshooting steps:

- Check the hardware
- Use IP config
- Use ping and tracert
- Perform DNS Check

More advanced approaches often involve looking at some of the networking performance counters, as explained below.

#### Network Counters

The table above gives you some reference points to better understand what you can expect out of your network. Here are some counters that can help you understand where the bottlenecks might exist:

| Counter | Description |
|---|---|
| Bytes Received/sec | The rate at which bytes are received over each network adapter. |
| Bytes Sent/sec | The rate at which bytes are sent over each network adapter. |
| Bytes Total/sec | The number of bytes sent and received over the network. |
| Segments Received/sec | The rate at which segments are received for the protocol |
| Segments Sent/sec | The rate at which segments are sent. |
| % Interrupt Time | The percentage of time the processor spends receiving and servicing hardware interrupts. This value is an indirect indicator of the activity of devices that generate interrupts, such as network adapters. |

> There is an important distinction between **latency** and **throughput**. **Latency** measures the time it takes for a packet to be transferred across the network, either in terms of a one-way transmission or a round-trip transmission. **Throughput** is different and attempts to measure the quantity of data being sent and received within a unit of time.

### Memory

| Counter | Description |
|---|---|
| Available MBs | This counter represents the amount of memory that is available to applications that are executing. Low memory can trigger Page Faults, whereby additional pressure is put on the CPU to swap memory to and from the disk. if the amount of available memory dips below 10%, more memory should be obtained. |
| Pages/sec | This is actually the sum of "Pages Input/sec" and "Pages Output/sec" counters which is the rate at which pages are being read and written as a result of pages faults. Small spikes with this value do not mean there is an issue but sustained values of greater than 50 can mean that system memory is a bottleneck. |
| Paging File(\_Total)\\% Usage | The percentage of the system page file that is currently in use. This is not directly related to performance, but you can run into serious application issues if the page file does become completely full and additional memory is still being requested by applications. |

## Key Performance Testing Activities

Performance testing activities vary depending on the subcategory of performance testing and the system's requirements and constraints. For specific guidance you can follow the link to the subcategory of performance tests listed above. The following activities might be included depending on the performance test subcategory:

### Identify the Acceptance Criteria for the Tests

This will generally include identifying the goals and constraints for the performance characteristics of the system.

### Plan and Design the Tests

In general we need to consider the following points:

- Defining the load the application should be tested with
- Establishing the metrics to be collected
- Establish what tools will be used for the tests
- Establish the performance test frequency: whether the performance tests be done as a part of the feature development sprints, or only prior to release to a major environment?

### Implementation

- Implement the performance tests according to the designed approach.
- Instrument the system and ensure that is emitting the needed performance metrics.

### Test Execution

- Execute the tests and collect performance metrics.

### Result Analysis and Re-testing

- Analyze the results/performance metrics from the tests.
- Identify needed changes to tweak the system (i.e., code, infrastructure) to better accommodate the test objectives.
- Then test again. This cycle continues until the test objective is achieved.

The [Iterative Performance Test Template](iterative-perf-test-template/) can be used to capture details about the test result for every iterations.

## Resources

- [Patterns and Practices: Performance Testing Guidance for Web Applications](https://learn.microsoft.com/en-us/archive/blogs/dajung/ebook-pnp-performance-testing-guidance-for-web-applications)

</section>
</details>

<details>
<summary>译文</summary>
<section>

# 性能测试

**来源：**[Microsoft Engineering Fundamentals Playbook — Performance Testing](https://github.com/microsoft/code-with-engineering-playbook)（开源，MIT 许可）
**组织：** Microsoft ISE Engineering Fundamentals Playbook
**最后更新：** 2024 年 8 月 22 日

---

性能测试（Performance Testing）是一个含义过载的术语，被用来指代若干类与性能相关的测试子类别，每一类都有不同的目的。

对整体性能测试的一个较好描述如下：

> “性能测试是一种测试类型，旨在确定系统在给定工作负载下的响应性（responsiveness）、吞吐量（throughput）、可靠性（reliability）和/或可扩展性（scalability）。” —— [《Web 应用性能测试指南》（Performance Testing Guidance for Web Applications）](https://learn.microsoft.com/en-us/archive/blogs/dajung/ebook-pnp-performance-testing-guidance-for-web-applications)

## 为什么要做性能测试

进行性能测试通常是为了达成以下一个或多个目标：

- **调优系统性能**
  - 识别系统在不同负载水平下的瓶颈和问题。
  - 比较系统在不同系统配置下的性能特征。
  - 为系统制定扩展（scaling）策略。
- 辅助**容量规划（capacity planning）**
  - 容量规划是确定运行一个应用以支撑预定义性能目标所需硬件和软件资源类型的过程。
  - 容量规划涉及识别业务预期、应用使用的周期性波动，并考虑运行硬件和软件基础设施的成本。
- 评估系统的**发布就绪度（readiness）**：
  - 在类生产环境中评估系统的性能特征（响应时间、吞吐量）。目标是确保在发布时能够达成性能目标。
- 评估**应用变更对性能的影响**
  - 将应用变更后的性能特征与此前运行（或基线值）的性能特征进行比较，可以提示变更所引入的性能问题（性能回归，performance regression）或性能改进。

## 关键性能测试类别

性能测试是一个宽泛的主题，可以在许多领域进行测试。概括地说，你可以对后端和前端进行测试，也可以测试单个组件的性能以及端到端的功能。

测试还有若干类别：

### 负载测试（Load Testing）

这是性能测试的一个子类别，专注于验证系统在面对生产运行期间预期负载量时的性能特征。**耐久性测试（Endurance Test）**或**浸泡测试（Soak Test）**是一种持续数小时到数天的长时间负载测试。

### 压力测试（Stress Testing）

这是性能测试的一个子类别，专注于验证系统在面对极端负载时的性能特征。其目标是评估系统在被压到极限时的表现——它是能够恢复（即横向扩展，scale-out），还是直接崩溃并失败？

### 耐久性测试（Endurance Testing）

耐久性测试的目标是确保系统能够在长时间负载下维持良好的性能。

### 尖峰测试（Spike Testing）

尖峰测试的目标是验证软件系统能够良好地应对大规模、突发的流量尖峰。

### 混沌测试（Chaos Testing）

混沌测试或混沌工程（Chaos engineering）是一种在系统上进行实验的实践，以建立对系统在生产环境中能够承受动荡条件的信心。其目标是在弱点演变为全系统性问题之前将其识别出来。开发者通常会为服务故障实现回退（fallback）流程。混沌测试会任意地关闭系统的不同部分，以验证回退流程能够正确运作。

## 最佳实践

进行性能测试时请考虑以下最佳实践：

- **一次只做一处变更。** 不要在两次测试之间对系统做多处变更。如果这样做，你将无法判断是哪一处变更导致了性能的提升或下降。
- **自动化测试。** 尽可能自动化性能测试运行所需的资源准备（setup）与清理（teardown）。手动执行可能导致配置错误。
- **使用不同的 IP 地址。** 某些系统会对来自单个 IP 地址的请求进行限流（throttle）。如果你测试的系统有这类限制，可以使用不同的 IP 地址来模拟多个用户。

## 性能监视器指标（Performance Monitor Metrics）

在执行各类测试方法时——无论是压力、耐久性、尖峰还是混沌测试——捕获各种指标以观察系统的表现都很重要。

在基础硬件层面，需要考虑四个领域：

- 物理磁盘（Physical disk）
- 内存（Memory）
- 处理器（Processor）
- 网络（Network）

这四个领域密不可分，意味着一个领域的性能不佳会导致另一个领域的性能不佳。关注理解应用性能的工程师应当聚焦于这四个核心领域。

一个领域性能影响另一个领域性能的经典例子是内存压力（memory pressure）。如果应用可用内存不足，操作系统会尝试通过将数据页从内存转移到磁盘来弥补内存短缺，从而释放内存。但这项工作需要 CPU 和物理磁盘的协助。这意味着当你观察内存不足时的性能时，也会注意到磁盘活动以及 CPU 的尖峰。

### 物理磁盘

几乎所有软件系统都依赖物理磁盘的性能，数据库的性能尤其如此。使用 SSD（固态硬盘）作为物理磁盘存储的更现代方法可以显著提升应用性能。以下是一些你可以捕获和分析的指标：

| 计数器 | 描述 |
|---|---|
| Avg. Disk Queue Length（平均磁盘队列长度） | 该值由 (Disk Transfers/sec)\*(Disk sec/Transfer) 计数器推导而来。该指标描述了一段时间内的磁盘队列，平滑了任何快速尖峰。任何物理磁盘的平均队列长度在长时间内超过 2，都可能表明你的磁盘是瓶颈。 |
| % Idle Time（空闲时间百分比） | 这是磁盘处于空闲状态的时间百分比，即没有来自操作系统的待处理磁盘请求等待完成。此处数值较低是一个积极信号，表明磁盘有富余容量来服务或写入来自操作系统的请求。 |
| Avg. Disk sec/Read 和 Avg. Disk sec/Write | 这两者都测量磁盘的延迟（latency）。延迟被定义为一次磁盘传输完成所需的平均时间。你显然希望数值尽可能低，但需要小心考虑 SSD 与传统机械磁盘之间固有的速度差异。对于这个计数器，重要的是在硬件安装后定义一个基线（baseline），之后使用该值来判断你是否遇到与硬件相关的延迟问题。 |
| Disk Reads/sec 和 Disk Writes/sec | 这些计数器分别测量每秒完成的 IO 请求总数。与延迟计数器类似，这些计数器的好坏值取决于你的磁盘硬件，但高于初始基线的值通常并不指向硬件问题。这个计数器可用于识别磁盘 IO 的尖峰。 |

### 处理器

理解在内核模式（kernel mode）或特权模式（privileged mode）中花费的时间量很重要。一般来说，如果代码花费过多时间执行操作系统调用，这可能是一个需要关注的领域，因为它会妨碍你运行用户模式（user mode）应用，例如数据库、Web 服务器/服务等。

指导原则是，CPU 只应花费约 20% 的总处理器时间在内核模式下运行。

| 计数器 | 描述 |
|---|---|
| % Processor time（处理器时间百分比） | 这是处理器忙于执行的总经过时间的百分比。这个计数器可能过高也可能过低。如果你的处理器时间持续低于 40%，那么就需要质疑你是否过度配置（over provision）了 CPU。70% 通常被认为是一个良好的目标值，如果你开始超过 70%，你可能需要探究为何存在高 CPU 压力。 |
| % Privileged (Kernel Mode) time（特权/内核模式时间百分比） | 这测量处理器在内核模式下执行所花费的经过时间百分比。由于该计数器只考虑内核操作，较高的特权时间百分比（大于 25%）可能表明存在应调查的驱动程序或硬件问题。 |
| % User time（用户时间百分比） | 处理器在用户模式下执行（你的应用代码）所花费的经过时间百分比。一个良好的指导原则是持续低于 65%，因为你希望为上述内核操作以及其他应用所需的任何突发 CPU 留出一些缓冲。 |
| Queue Length（队列长度） | 这是已准备好执行但正在等待核心可用的线程数。在单核机器上，持续大于 2-3 的值可能意味着你存在一些 CPU 压力。类似地，对于多核机器，将队列长度除以核心数，如果该值持续大于 2-3，则可能存在 CPU 压力。 |

### 网络适配器

网络速度往往是性能不佳的隐藏元凶。找到网络性能不佳的根本原因通常很困难。问题的来源可能来自带宽占用大户，例如视频会议、事务数据、网络备份、娱乐视频。

事实上，网络变慢的三个最常见原因是：

- 拥塞（Congestion）
- 数据损坏（Data corruption）
- 冲突（Collisions）

一些可以提供帮助的工具包括：

- ifconfig
- netstat
- iperf
- tcpretrans
- tcpdump
- WireShark

网络性能故障排查通常从检查硬件开始。通常要探查的是是否存在松动的线缆，或检查所有路由器是否已通电。并非总能做到，但有时简单地重启调制解调器或路由器就能解决许多问题。

网络专家通常执行以下故障排查步骤序列：

- 检查硬件
- 使用 IP config
- 使用 ping 和 tracert
- 执行 DNS 检查

更高级的方法通常涉及查看一些网络性能计数器，如下所述。

#### 网络计数器

上表为你提供了一些参考点，以更好地理解你可以从网络中预期到什么。以下是一些可以帮助你理解瓶颈可能存在于何处的计数器：

| 计数器 | 描述 |
|---|---|
| Bytes Received/sec | 每个网络适配器接收字节的速率。 |
| Bytes Sent/sec | 每个网络适配器发送字节的速率。 |
| Bytes Total/sec | 网络上发送和接收的字节数。 |
| Segments Received/sec | 协议接收分段的速率。 |
| Segments Sent/sec | 发送分段的速率。 |
| % Interrupt Time（中断时间百分比） | 处理器花费在接收和服务硬件中断上的时间百分比。该值是产生中断的设备（如网络适配器）活动的间接指标。 |

> **延迟（latency）**与**吞吐量（throughput）**之间有一个重要区别。**延迟**衡量一个数据包在网络中传输所需的时间，可以是单向传输或往返传输。**吞吐量**则不同，它试图衡量单位时间内发送和接收的数据量。

### 内存

| 计数器 | 描述 |
|---|---|
| Available MBs（可用兆字节） | 该计数器表示可供正在执行的应用使用的内存量。低内存可能触发页面错误（Page Faults），从而给 CPU 带来额外压力，使其在内存和磁盘之间交换内存。如果可用内存量低于 10%，则应获取更多内存。 |
| Pages/sec（每秒页数） | 这实际上是“Pages Input/sec”和“Pages Output/sec”计数器之和，即由于页面错误而读写页面的速率。该值的小幅尖峰并不意味着存在问题，但持续大于 50 的值可能意味着系统内存是瓶颈。 |
| Paging File(\_Total)\\% Usage（页面文件使用百分比） | 系统页面文件当前正在使用的百分比。这与性能没有直接关系，但如果页面文件确实完全填满且应用仍在请求额外内存，你可能会遇到严重的应用问题。 |

## 关键性能测试活动

性能测试活动因性能测试子类别以及系统的需求和约束而异。具体指导可参考上文列出的性能测试子类别链接。根据性能测试子类别的不同，可能包括以下活动：

### 识别测试的验收标准

这通常包括识别系统性能特征的目标和约束。

### 规划和设计测试

一般来说，我们需要考虑以下几点：

- 定义应用应测试的负载
- 确定要收集的指标
- 确定测试将使用的工具
- 确定性能测试频率：性能测试是作为功能开发冲刺（sprint）的一部分进行，还是仅在发布到主要环境之前进行？

### 实现

- 根据设计的方法实现性能测试。
- 对系统进行埋点（instrument），并确保其发出所需的性能指标。

### 测试执行

- 执行测试并收集性能指标。

### 结果分析与重新测试

- 分析测试的结果/性能指标。
- 识别调整系统（即代码、基础设施）所需的变更，以更好地满足测试目标。
- 然后再次测试。这个循环持续进行，直到测试目标达成。

可以使用[迭代性能测试模板（Iterative Performance Test Template）](iterative-perf-test-template/)来记录每次迭代的测试结果详情。

## 资源

- [Patterns and Practices：Web 应用性能测试指南](https://learn.microsoft.com/en-us/archive/blogs/dajung/ebook-pnp-performance-testing-guidance-for-web-applications)

</section>
</details>

## 摘要

本文是微软 ISE（Industry Solutions Engineering，行业解决方案工程）团队维护的《Code With Engineering Playbook》中关于性能测试的一篇工程实践指南。文章首先引用微软 2007 年《Web 应用性能测试指南》中的定义，将性能测试界定为“确定系统在给定工作负载下的响应性、吞吐量、可靠性和/或可扩展性”的测试类型，随后系统性地阐述了性能测试的四大目的（调优、容量规划、发布就绪度评估、变更影响评估）、五大测试类别（负载、压力、耐久性、尖峰、混沌测试）、三条最佳实践，以及物理磁盘、处理器、网络、内存四大硬件领域的性能监视器指标与经验阈值。文章最后给出性能测试活动的完整流程（验收标准、规划、实现、执行、结果分析与重测）。其核心价值在于为工程团队提供一份可直接落地的性能测试操作清单与指标参考，但其中部分经验阈值（如 20% 内核时间、40%/70% CPU 阈值）与微软官方文档存在出入，需谨慎对待。

## 术语表

| 术语 | 全称 | 解释 |
| :--- | :--- | :--- |
| Performance Testing | - | 性能测试。一种非功能性测试实践，用于评估工作负载在各种条件下的行为表现，通过测量响应时间、吞吐量、资源使用率和稳定性来证明系统持续达到既定目标。 |
| Load Testing | - | 负载测试。验证系统在正常和峰值使用情况下能否处理预期用户量的测试，揭示基线性能、容量上限和扩展的有效性。 |
| Stress Testing | - | 压力测试。在系统达到或超过预期工作负载极限、或资源可用性降低的情况下评估系统行为的测试，用于揭示最大容量、故障模式和恢复行为。 |
| Endurance Testing / Soak Test | - | 耐久性测试（又称浸泡测试）。在显著负载下持续显著时间段以确定系统稳定性的测试，用于检测内存泄漏、资源耗尽、连接池问题等仅在长时间运行后才出现的问题。 |
| Spike Testing | - | 尖峰测试。确定系统从峰值负载的突然爆发中恢复并回到稳定状态能力的测试，用于验证系统对突发流量尖峰的响应。 |
| Chaos Testing / Chaos Engineering | - | 混沌测试/混沌工程。在分布式系统上进行实验以建立对系统承受生产环境动荡条件信心的实践。术语由 Netflix 团队于 2015 年正式提出，先驱工具为 2011 年的 Chaos Monkey。 |
| Capacity Planning | - | 容量规划。预测服务资源需求并为其保障资源供应的过程，即确定运行应用以支撑预定义性能目标所需硬件和软件资源类型。 |
| Throughput | - | 吞吐量。系统处理需求的速率，通常以“每秒请求数”衡量，关注单位时间内能处理多少请求。 |
| Latency | - | 延迟。处理一个请求并返回响应所需的时间，关注单个请求多快完成。与吞吐量并非简单反比关系。 |
| Responsiveness | - | 响应性。系统对用户输入做出快速反应的能力，强调整个输入-输出循环的低延迟，用户感知的响应性才是真正重要的。 |
| Scalability | - | 可扩展性。工作负载动态改变其容量上限以适应不同需求水平的能力，分为垂直扩展（scale up/down）和水平扩展（scale out/in）。 |
| Performance Regression | - | 性能回归。与已建立的基线相比，由代码、配置或基础设施变更引入的性能下降。 |
| Baseline | - | 基线。代表工作负载在正常条件下行为的一组指标，是后续测试比较的固定参照点。 |
| Bottleneck | - | 瓶颈。系统中限制整体性能的环节，例如磁盘队列长度持续过高表明磁盘成为瓶颈。 |
| Page Fault | - | 页面错误（缺页）。程序访问的内存页不在物理内存中时触发的事件，硬缺页需从磁盘读取，会带来额外 CPU 和磁盘压力。 |
| Kernel Mode / Privileged Mode | - | 内核模式/特权模式。操作系统内核代码执行的模式，拥有对硬件的完全访问权限。与之相对的是用户模式（User Mode），即应用代码执行的受限模式。 |
| SSD | Solid State Drive | 固态硬盘。使用闪存而非机械旋转盘片的存储设备，可显著提升应用尤其是数据库的性能。 |
| Microsoft ISE | Industry Solutions Engineering | 微软行业解决方案工程团队，与客户并肩解决云端与边缘端最棘手的技术问题，是《Code With Engineering Playbook》的维护者。 |
| Patterns & Practices | - | 微软模式与实践团队，负责为开发者提供经过验证的工程实践指南、框架和参考实现，本文引用的《Web 应用性能测试指南》即出自该团队。 |
| iperf | - | 网络带宽测量工具，通过客户端-服务器模式主动测量 IP 网络的最大可达带宽，支持 TCP、UDP、SCTP 吞吐量测试。 |
| tcpdump | - | 命令行数据包分析器（抓包工具），打印匹配过滤表达式的网络数据包内容，可保存为 pcap 文件供后续分析。 |
| Wireshark | - | 全球最知名的网络协议分析器，免费开源（GPL v2），1997 年由 Gerald Combs 创建（原名 Ethereal，2006 年更名）。 |
| netstat | - | 网络统计命令，打印网络连接、路由表、接口统计等信息，在现代 Linux 中已被 `ss` 等工具逐步取代。 |
| ifconfig | - | 网络接口配置命令，用于查看和配置网络接口的 IP 地址、子网掩码等参数。 |
| tcpretrans | - | TCP 重传追踪工具，由 Brendan Gregg 编写，使用 ftrace 动态插桩内核函数以追踪 TCP 重传，用于定位网络丢包与重传问题。 |
| DNS | Domain Name System | 域名系统。将域名解析为 IP 地址的分布式命名系统，DNS 故障排查是网络性能排查的常见步骤之一。 |
| tracert | - | 路由追踪命令（Unix 中为 traceroute），通过递增 TTL 值发送探测包来映射数据包到达目的地所经过的每一跳路由器。 |
| Page File / Paging File | - | 页面文件/分页文件。操作系统在磁盘上用于扩展物理内存的虚拟内存文件，内存不足时数据页会被换入换出该文件。 |
| Disk Queue Length | - | 磁盘队列长度。描述磁盘队列随时间变化的指标，由磁盘传输速率与每次传输时间推导，持续过高表明磁盘成为瓶颈。 |

## 深度解读

### 核心论点与论证逻辑

本文的核心论点可以概括为：**性能测试是一套由多个子类别构成的系统工程实践，其有效性取决于对硬件四大领域（磁盘、内存、处理器、网络）指标的持续观测，以及对测试流程的规范化执行**。

文章的论证逻辑是典型的“定义—分类—方法—指标—流程”递进结构。它先引用权威定义锚定“性能测试”的内涵，再通过“为什么要做”建立价值主张，随后将性能测试拆解为负载、压力、耐久性、尖峰、混沌五个子类别，并给出三条可操作的最佳实践。文章的重心落在“性能监视器指标”一节，用四张表格分别列出磁盘、处理器、网络、内存的关键计数器及其经验阈值，最后以“关键性能测试活动”收束为一个迭代闭环。

这一逻辑的优点是**实用导向**：读者可以按图索骥地知道“测什么、看什么指标、阈值是多少”。但它的论据强度存在明显的不均衡——五大测试类别的定义较为严谨（与 ISTQB、Microsoft Learn 的正式定义一致），而指标阈值部分则大量依赖经验值，且部分数值与微软官方文档存在出入（详见下文“真实性评估”）。因此，本文更适合作为一份**入门级操作清单**，而非精确的调优基准。

### 背景与语境：从 2007 年 P&P 指南到 2024 年 Playbook

本文的“血统”值得关注。它开篇引用的定义出自微软 patterns & practices（P&P）团队 2007 年 9 月出版的《Web 应用性能测试指南》（Performance Testing Guidance for Web Applications），作者为 J.D. Meier、Carlos Farre 等五人。P&P 是微软内部专门产出工程实践指南的团队，其文档后来被归档到 Microsoft Learn 的 “msp-n-p” 分区。

而本文本身出自微软 ISE（Industry Solutions Engineering）团队维护的《Code With Engineering Playbook》。ISE 团队自述“一只脚在微软，一只脚在开源社区”，其 Playbook 是用于 “code-with” 客户/合作伙伴项目的工程实践手册，仓库创建于 2018 年 7 月 30 日。这意味着本文是**微软内部工程实践知识从封闭走向开源的一个样本**——它把 2007 年的经典指南重新提炼、压缩成一份面向现代云原生团队的速查手册。

值得注意的是，本文的指标阈值（如 20% 内核时间、40%/70% CPU 阈值）与 2007 年 P&P 指南的原始内容并不完全一致，更像是作者在多年实践基础上重新归纳的经验值。这种“传承中的再加工”恰恰是本文可信度需要审慎对待的地方：它继承了权威来源的框架，但具体数值的权威性打了折扣。

### 技术维度：四大硬件领域的联动逻辑

文章最有价值的技术洞见，是它对磁盘、内存、处理器、网络四大领域“密不可分”关系的强调，并以内存压力为例做了清晰的因果推演：**可用内存不足 → 操作系统将数据页换出到磁盘（页面错误/分页）→ 需要 CPU 和磁盘协同工作 → 表现为磁盘活动与 CPU 的同步尖峰**。

这一“牵一发而动全身”的视角，是性能调优中最容易被初学者忽视、也最考验工程师功力的地方。例如，一个看似“CPU 占用过高”的问题，其根因可能根本不是 CPU，而是内存不足导致的频繁分页；一个“磁盘 IO 尖峰”的背后，可能是内存压力在驱动换页。文章通过这个例子，实际上在教导读者**不要孤立地看单个指标，而要建立跨领域的因果关联**。

在具体指标层面，文章给出的阈值（磁盘队列长度 > 2、处理器队列长度 > 2-3、可用内存 < 10%、Pages/sec > 50 等）大多源自 Windows 性能监视器（Performance Monitor）的经典经验值，其中磁盘队列长度、处理器队列长度、可用内存阈值与微软官方文档基本一致，属于可靠的经验法则；而内核时间 20%、CPU 时间 40%/70% 等阈值则与微软官方文档存在偏差（详见真实性评估）。

### 争议与分歧：经验阈值的权威性存疑

本文最值得商榷的部分，是处理器一节给出的几个具体阈值。经与微软官方文档交叉验证，存在以下分歧：

- **“CPU 应只花费约 20% 时间在内核模式”**：微软官方文档（Microsoft Learn 归档博客）给出的阈值是**特权时间超过 30%** 才表明高 IO/驱动活动，20% 这一数字在微软官方来源中找不到依据，疑似与“80% 总处理器时间”指南中“留出 20% 余量”的概念相混淆。
- **“处理器时间低于 40% 即过度配置、70% 为目标、高于 70% 即高压”**：微软官方文档（《Troubleshoot issues using Performance Monitor》）给出的分档是 **0-50% 健康、50-80% 监控/警告、80-100% 严重**，40% 和 70% 这两个具体阈值并非微软官方标准。
- **“用户时间应持续低于 65%”**：这一数字来自第三方（MSSQLTips），微软官方对 % User Time 的分档是 **<50% 健康、50-80% 警告、>80% 严重**。

这些分歧并不意味着文章“错误”，而是说明**性能阈值本身高度依赖具体硬件、工作负载和业务目标，不存在放之四海而皆准的“标准值”**。文章将这些经验值以“指导原则（guideline）”的口吻呈现，本身是谨慎的，但读者若将其当作硬性标准，则可能误判。这提醒我们：性能调优中的阈值应当**先建立自己的基线，再以基线为参照判断异常**，而非机械套用他人的经验数字——这一点文章在磁盘延迟计数器一节其实也明确提到了“定义基线”的重要性，只是未将这一原则贯彻到所有指标上。

### 实践指导价值

尽管存在阈值权威性的瑕疵，本文的实践价值仍然突出，尤其体现在以下三点：

1. **测试类别的清晰划分**：负载、压力、耐久性、尖峰、混沌五类测试各有明确目的，帮助团队避免“只做负载测试就以为覆盖了性能测试”的常见误区。例如，一个系统通过了负载测试，却可能在长时间运行后因内存泄漏而崩溃（需耐久性测试），或在突发流量下雪崩（需尖峰测试），或在依赖服务故障时无法降级（需混沌测试）。
2. **最佳实践的三条铁律**：“一次只改一处”“自动化测试”“使用不同 IP 模拟多用户”，都是性能测试中极易踩坑的实操细节，尤其是“一次只改一处”直接关系到能否归因性能变化。
3. **迭代闭环的流程框架**：从验收标准到结果分析与重测的完整流程，与 2007 年 P&P 指南的七步活动一脉相承，为团队提供了可复用的项目管理模板。

### 真实性评估

| 声明/事实 | 验证状态 | 说明 |
| :--- | :--- | :--- |
| 性能测试定义引文（“responsiveness, throughput, reliability, and/or scalability … under a given workload”） | 已验证 | 逐字核实无误，出自微软 P&P 团队 2007 年《Web 应用性能测试指南》Chapter 1 Overview。 |
| 该指南的作者与出版时间（P&P 团队，2007 年 9 月） | 已验证 | 作者为 J.D. Meier、Carlos Farre 等五人，页面标注 “September 2007”。 |
| “CPU 应只花费约 20% 时间在内核模式” | 存疑 | 微软官方阈值是特权时间 >30% 才表明高 IO/驱动活动，20% 无官方依据，疑似与“80% 总处理器时间”的 20% 余量概念混淆。 |
| “处理器时间 <40% 过度配置、70% 目标、>70% 高压” | 存疑 | 微软官方分档为 0-50% 健康、50-80% 监控、80-100% 严重，40%/70% 非官方标准。 |
| “特权时间 >25% 可能表明驱动/硬件问题” | 部分验证 | 第三方（MSSQLTips）有此说法，微软官方阈值为 30%，且归因于 IO/驱动活动而非“硬件”。 |
| “用户时间应持续低于 65%” | 部分验证 | 来自第三方（MSSQLTips），微软官方对 % User Time 分档为 <50% 健康。 |
| “处理器队列长度持续 >2-3 表明 CPU 压力” | 已验证 | 微软官方（AskPerf）确认“持续大于 2 通常表明处理器拥塞”，且需按核心数归一化。 |
| “磁盘队列长度长时间 >2 表明磁盘瓶颈” | 已验证 | 微软 Windows 2000 Server 运维指南确认“超过主轴数两倍即瓶颈”，单盘即 >2。 |
| “可用内存 <10% 应增加内存” | 已验证 | 微软 PerfGuide 确认可用内存低于物理内存 10% 会增加对磁盘的依赖。 |
| “Pages/sec 持续 >50 表明内存瓶颈” | 部分验证 | 微软官方阈值与磁盘速度相关（慢盘 >40、快盘 >300），50 是简化值。 |
| “内存压力导致换页、增加 CPU 和磁盘活动” | 已验证 | 微软官方（AskPerf）确认内存不足导致过多页面错误和磁盘争用。 |
| “网络变慢的三个最常见原因：拥塞、数据损坏、冲突” | 已验证 | Allied Telesis 官方故障排查指南明确列出这三大原因（另有 STP 拓扑变更通知为第四原因）。 |
| 本文许可证为 “MIT” | 部分验证 | 仓库实为双许可：文档 CC-BY-4.0，代码 MIT，页面标注 “MIT-licensed” 仅对代码部分成立。 |

### 总结

本文是微软 ISE 团队面向工程实践的一份性能测试速查手册，其价值在于以清晰的“定义—分类—方法—指标—流程”结构，为团队提供了一份可直接落地的性能测试操作清单，尤其是对磁盘、内存、处理器、网络四大领域联动关系的强调，以及负载/压力/耐久性/尖峰/混沌五类测试的清晰划分，具有很高的入门指导价值。但文章在处理器指标阈值上存在与微软官方文档不一致的经验值，且许可证标注不够准确，读者应将其视为**经验参考而非权威标准**，并在实践中以自建基线为判断依据。

**关键要点：**

- 性能测试是包含负载、压力、耐久性、尖峰、混沌等多个子类别的系统工程实践，各子类别目的不同，不可相互替代。
- 磁盘、内存、处理器、网络四大硬件领域密不可分，内存压力会通过换页机制联动引发 CPU 和磁盘的同步尖峰，调优需建立跨领域因果视角。
- 文章部分经验阈值（20% 内核时间、40%/70% CPU 阈值、65% 用户时间）与微软官方文档存在出入，应视为经验参考，并以自建基线为判断依据。

## 参考资料

- [Performance Testing Guidance for Web Applications（主页面）](https://learn.microsoft.com/en-us/previous-versions/msp-n-p/bb924375(v=pandp.10)) — 本文引用的性能测试定义出处，微软 P&P 团队 2007 年出版。
- [Chapter 1 – Fundamentals of Web Application Performance Testing](https://learn.microsoft.com/en-us/previous-versions/msp-n-p/bb924356(v=pandp.10)) — 引文逐字出处章节。
- [microsoft/code-with-engineering-playbook（GitHub）](https://github.com/microsoft/code-with-engineering-playbook) — 本文所属仓库，含 LICENSE（CC-BY-4.0）与 LICENSE-CODE（MIT）双许可。
- [docs/ISE.md](https://github.com/microsoft/code-with-engineering-playbook/blob/main/docs/ISE.md) — 微软 ISE 团队背景说明。
- [Microsoft Learn — Architecture Strategies for Performance Testing](https://learn.microsoft.com/en-us/azure/well-architected/performance-efficiency/performance-test) — 性能测试、负载、压力、尖峰、耐久性、基线、回归等术语的官方定义。
- [Microsoft Learn — Troubleshoot issues using Performance Monitor](https://learn.microsoft.com/en-us/troubleshoot/windows-server/support-tools/troubleshoot-issues-performance-monitor) — CPU 0-50%/50-80%/80-100% 官方分档来源。
- [Microsoft Learn — Choose Your Own Adventure: User Mode Versus Privileged Mode Processor Usage](https://learn.microsoft.com/en-us/archive/blogs/clinth/choose-your-own-adventure-user-mode-versus-privileged-mode-processor-usage) — 特权时间 >30% 官方阈值来源。
- [Microsoft Community Hub — An Overview of Processor Bottlenecks](https://techcommunity.microsoft.com/blog/askperf/an-overview-of-processor-bottlenecks/372650) — 处理器队列长度 >2 官方依据。
- [Microsoft Community Hub — An Overview of Troubleshooting Memory Issues](https://techcommunity.microsoft.com/blog/askperf/an-overview-of-troubleshooting-memory-issues/372673) — 内存压力与 Pages/sec 官方依据。
- [Netflix Tech Blog — Chaos Engineering Upgraded](https://netflixtechblog.com/chaos-engineering-upgraded-878d341f15fa) — 混沌工程术语的正式提出来源。
- [Google SRE Book — Monitoring Distributed Systems](https://sre.google/sre-book/monitoring-distributed-systems/) — 吞吐量、延迟、四大黄金信号的权威定义。
- [Allied Telesis — Troubleshoot Slow Network Performance](https://www.alliedtelesis.com/sites/default/files/documents/configuration-guides/howto_aw-_troubleshoot_slow_network_performancerevb.pdf) — 网络变慢三大原因（拥塞、数据损坏、冲突）的官方依据。
- [iperf3 官方文档](https://software.es.net/iperf/) — iperf 网络带宽测量工具的官方说明。
- [tcpdump 官方 man page](https://www.tcpdump.org/manpages/tcpdump.1.html) — tcpdump 抓包工具的官方说明。
- [Wireshark 官方文档](https://www.wireshark.org/docs/) — Wireshark 网络协议分析器的官方说明。
- [Brendan Gregg — tcpretrans（perf-tools）](https://github.com/brendangregg/perf-tools/blob/master/net/tcpretrans) — tcpretrans TCP 重传追踪工具的来源。
