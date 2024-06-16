import auth from "./functions/auth";
import entered from "./functions/entered";

const middlewares = {
    auth, entered
}

export const middlewareTypes = {
    AUTH: 'auth',
    ENTERED: 'entered'
}

export const middleware = (to, from, next, isAuth) => {
    const usedMiddleware = to?.meta?.middleware || false;

    if (!usedMiddleware) {
        return next();
    }

    middlewares[usedMiddleware](next, isAuth);
}