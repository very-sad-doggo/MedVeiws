FROM postgres:15
HEALTHCHECK --interval=10s --timeout=3s CMD /usr/local/bin/pg_isready --username=django || exit 1