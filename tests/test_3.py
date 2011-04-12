import microactor


@microactor.reactive
def main(reactor):
    rc, stdout, stderr = yield reactor.proc.run(["/bin/ls"])
    print rc
    print repr(stdout)
    print repr(stderr)


if __name__ == "__main__":
    reactor = microactor.get_reactor()
    reactor.jobs.schedule(5, reactor.stop)
    reactor.run(main)


