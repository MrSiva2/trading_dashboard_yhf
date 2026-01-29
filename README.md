we will not be using direct threading. instead, we will use QThread + QObject
we will be using one worker per task type (trainingworker, backtestworker,liveworker)
