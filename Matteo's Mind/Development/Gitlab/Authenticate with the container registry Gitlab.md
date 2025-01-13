# From Local
To authenticate, run the `docker login` command. For example:

```
TOKEN=<token>
echo "$TOKEN" | docker login registry.example.com -u <username> --password-stdin
```

# With Pipeline

To use CI/CD to authenticate with the container registry, you can use:

- The `CI_REGISTRY_USER` CI/CD variable.
    
    This variable holds a per-job user with read-write access to the container registry. Its password is also automatically created and available in `CI_REGISTRY_PASSWORD`.
    
    ```
    echo "$CI_REGISTRY_PASSWORD" | docker login $CI_REGISTRY -u $CI_REGISTRY_USER --password-stdin
    ```
    
- A [CI job token](https://docs.gitlab.com/ee/ci/jobs/ci_job_token.html).
    
    ```
    echo "$CI_JOB_TOKEN" | docker login $CI_REGISTRY -u $CI_REGISTRY_USER --password-stdin
    ```
    
- A [deploy token](https://docs.gitlab.com/ee/user/project/deploy_tokens/index.html#gitlab-deploy-token) with the minimum scope of:
    
    - For read (pull) access, `read_registry`.
    - For write (push) access, `read_registry` and `write_registry`.
    
    ```
    echo "$CI_DEPLOY_PASSWORD" | docker login $CI_REGISTRY -u $CI_DEPLOY_USER --password-stdin
    ```
    
- A [personal access token](https://docs.gitlab.com/ee/user/profile/personal_access_tokens.html) with the minimum scope of:
    
    - For read (pull) access, `read_registry`.
    - For write (push) access, `read_registry` and `write_registry`.
    
    ```
    echo "<access_token>" | docker login $CI_REGISTRY -u <username> --password-stdin
    ```