# Quadlets (Systemd)

when in need to login add credential to the file in 

```bash
/etc/containers/auth.json
```

format is:
```json
{
	"auths": {
		"my-registry.local/foo/bar/image": {
			"auth": "…"
		},
		"my-registry.local/foo": {
			"auth": "…"
		},
		"my-registry.local": {
			"auth": "…"
		},
	}
}
```

```
Each entry contains a single hostname (e.g., `docker.io`) or a namespace (e.g., `quay.io/user/image`) as a key, and credentials in the form of a base64-encoded string as value of `auth`. The base64-encoded string contains a concatenation of the username, a colon, and the password.
```


> [!NOTE] the username, a colon, and the password.
https://github.com/containers/image/blob/main/docs/containers-auth.json.5.md