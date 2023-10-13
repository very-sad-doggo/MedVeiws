FROM postgres:15
HEALTHCHECK --interval=10s --timeout=3s CMD /bin/bash pg_isready --username=django || exit 1