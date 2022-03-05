from data.for_tasks import User, Jobs
from data.db_session import create_session, global_init

global_init('db/mars_explorer.db')
session = create_session()

job1 = Jobs()
job1.team_leader = 1
job1.job = 'deployment of residential modules 1 and 2'
job1.work_size = 15
job1.collaborators = '2, 3'
job1.is_finished = False
session.add(job1)
session.commit()
session.close()