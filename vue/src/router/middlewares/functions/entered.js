export default (next, isAuth) => {

    if (isAuth) {
        return next('/')
    }

    next()
}