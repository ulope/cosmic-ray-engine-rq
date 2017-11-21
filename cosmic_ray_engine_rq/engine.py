import time
from logging import getLogger

from cosmic_ray.execution.execution_engine import ExecutionEngine
from cosmic_ray.work_record import WorkRecord

from cosmic_ray_engine_rq.worker import cr_rq_worker


log = getLogger(__name__)


class RQExecutionEngine(ExecutionEngine):
    def __call__(self, timeout, pending_work, config):
        jobs = {
            cr_rq_worker.delay(dict(work_item), timeout, config)
            for work_item in pending_work
        }
        log.info("Queued %d jobs", len(jobs))

        start = time.monotonic()
        while jobs:
            time.sleep(.5)
            if (time.monotonic() - start) >= 10:
                log.info("Remaining jobs: %d", len(jobs))
                start = time.monotonic()
            finished = set()
            for job in jobs:
                if job.result:
                    result = WorkRecord(job.result)
                    log.info("Got result: %s: %s", result['command_line'], result['test_outcome'])
                    yield result
                    finished.add(job)
            jobs -= finished
