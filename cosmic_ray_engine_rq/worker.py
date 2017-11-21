from cosmic_ray.worker import worker_process
from redis.client import StrictRedis
from rq.decorators import job


@job('cosmic_ray', connection=StrictRedis())
def cr_rq_worker(work_item, timeout, config):
    return dict(worker_process(work_item, timeout, config))

