from prefect import Flow

from tasks.src import job

if __name__ == "__main__":
    with Flow("Example Job") as flow:
        job.run_example_job()

    flow.register(project_name="Example Pipeline")
    flow.run()
