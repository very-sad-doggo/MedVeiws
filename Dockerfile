FROM postgres:14-alpine
HEALTHCHECK --interval=10s --timeout=3s CMD /usr/local/bin/pg_isready --username=django || exit 1