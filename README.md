# $ noDB_
As the name suggest, a database which isn't one per se.

## what?
noDB is a database, which isn't.

## why?
inspired by Kevin Kuchta's [URL shortener](http://kevinkuchta.com/_site/2018/03/lambda-only-url-shortener/) using only AWS Lambdas.

## how?

at the heart of noDB is the [`DATA`](https://github.com/Sayan98/noDB/blob/5d3366f1086878c5a9c5cfcc01486af1e6a71809/src/noDB.py#L10) variable of [src/noDB.py](/src/noDB.py)

once changes are committed, the original src/noDB.py gets overwritten, this updated file stores the created records as serialised data in the `DATA` variable.

every commit leads to a change of the previously updated src/noDB.py file to reflect the changes as necessary!


:octocat:
