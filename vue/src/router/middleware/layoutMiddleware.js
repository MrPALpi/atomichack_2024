
import { layoutMap, layoutTypes } from "../../layouts/layoutTypes";

export async function layoutMiddleware(route) {
    const { layout } = route.meta;
    const layoutName = layout || layoutTypes.DEFAULT;
    const fileName = layoutMap[layoutName];
    const component = await import(`../../layouts/${fileName}`);
    route.meta.layoutComponent = component.default;
}
