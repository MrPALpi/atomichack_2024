import middlewares  from './index'

export default (to, next, isAuth) => {

    const usedMiddleware = to?.meta?.middleware;
    const authRequired = !!usedMiddleware?.includes(middlewares.AUTH);

    console.log(authRequired, isAuth)
  
    if (isAuth || !authRequired) {
        return next();
    }

    next('/auth')
}