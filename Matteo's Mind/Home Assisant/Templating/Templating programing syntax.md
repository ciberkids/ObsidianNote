Jinja has multiple ways to [control whitespace](https://jinja.palletsprojects.com/en/3.0.x/templates/#whitespace-control). It _does not_ have a way to prettify output, you have to manually make sure everything looks "nice".

The broadest solution is to set `trim_blocks` and `lstrip_blocks` on the env.

```python
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True
```

If you want to keep a newline at the end of the file, set `strip_trailing_newlines = False`.

You can use control characters to modify how the whitespace around a tag works. `-` always removes whitespace, `+` always preserves it, overriding the env settings for that tag. The `-` character can go at the beginning or end (or both) of a tag to control the whitespace in that direction, the `+` character only makes sense at the beginning of a tag.

- `{%- if ... %}` strips before
- `{%- if ... -%}` strips before and after
- `{%+ if ... %}` preserves before
- `{%+ if ... -%}` preserves before and strips after
- remember that `{% endif %}` is treated separately

# functions
https://jinja.palletsprojects.com/en/latest/templates/#list-of-builtin-filters

# Tools
https://j2live.ttl255.com/