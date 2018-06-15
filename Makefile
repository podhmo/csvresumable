SUBDIRS := $(dir $(shell find . -name Makefile -mindepth 2 ))

define runT
	echo '```console' > $(1)readme.md
	make -C $(1) 2>/dev/stdout | sed 's@$(shell echo $$HOME)@$$HOME@g' >> $(1)readme.md
	echo '```' >> $(1)readme.md

endef

runall:
	$(foreach d,${SUBDIRS},$(call runT,$(d)))

readme:
	$(MAKE) -C examples/readme
	cp examples/readme/readme.md README.md
.PHONY: readme
