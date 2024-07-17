Timsort є найбільш ефективним алгоритмом сортування серед трьох, оскільки він поєднує в собі переваги сортування злиттям і вставками. 
Це робить його швидким та ефективним як для великих, так і для майже відсортованих масивів, що і є причиною використання цього алгоритму в Python. 
Програмісти часто покладаються на вбудовані функції сортування саме через їх оптимізовану продуктивність та надійність.

Results:

Testing with array size: 100
Insertion sort time for size 100: 0.00040579999949841294
Merge sort time for size 100: 0.0003114000010100426     
Timsort time for size 100: 1.9999999494757503e-05  
     
Testing with array size: 1000
Insertion sort time for size 1000: 0.049375399999917136
Merge sort time for size 1000: 0.004144299999097711
Timsort time for size 1000: 0.001797499999156571

Testing with array size: 10000
Insertion sort time for size 10000: 4.660787200000414
Merge sort time for size 10000: 0.059191500000451924
Timsort time for size 10000: 0.0029281999995873775