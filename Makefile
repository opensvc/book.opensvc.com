OM:=om

all: kw build

kw:
	(echo '# Keywords Reference: node\n\n<!-- toc -->\n\n' ;sudo ${OM} node doc --depth 1) > src/agent.reference.keywords.node.md
	(echo '# Keywords Reference: cluster\n\n<!-- toc -->\n\n' ;sudo ${OM} cluster doc --depth 1) > src/agent.reference.keywords.cluster.md
	(echo '# Keywords Reference: svc\n\n<!-- toc -->\n\n' ;sudo ${OM} svc doc --depth 1) > src/agent.reference.keywords.svc.md
	(echo '# Keywords Reference: vol\n\n<!-- toc -->\n\n' ;sudo ${OM} vol doc --depth 1) > src/agent.reference.keywords.vol.md
	(echo '# Keywords Reference: cfg\n\n<!-- toc -->\n\n' ;sudo ${OM} cfg doc --depth 1) > src/agent.reference.keywords.cfg.md
	(echo '# Keywords Reference: sec\n\n<!-- toc -->\n\n' ;sudo ${OM} sec doc --depth 1) > src/agent.reference.keywords.sec.md
	(echo '# Keywords Reference: usr\n\n<!-- toc -->\n\n' ;sudo ${OM} usr doc --depth 1) > src/agent.reference.keywords.usr.md

build:
	PATH=. ./mdbook build
