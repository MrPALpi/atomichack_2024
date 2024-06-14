const options = {
  year: 'numeric',
  month: 'long',
  day: 'numeric',
};

export default (date=null, type=options, locale='ru-RU')=> {
    if (date === null) {
        return '';
    }

    return new Date(date).toLocaleDateString(locale, type)
}