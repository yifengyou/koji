#!/bin/bash

set -x

koji build anolis8-addons --skip-tag  --nowait   'git+https://gitee.com/src-anolis-os/bash#origin/a8'

exit 0

koji build anolis8-addons --skip-tag  --nowait   'git+https://gitee.com/src-anolis-os/kernel#origin/a8'

koji build anolis8-addons --skip-tag  --nowait   'git+https://gitee.com/src-anolis-os/binutils#origin/a8'

koji build anolis8-addons --skip-tag  --nowait   'git+https://gitee.com/src-anolis-os/anolis-release#origin/a8'

koji build anolis8-addons --skip-tag  --nowait   'git+https://gitee.com/src-anolis-os/curl#origin/a8'

