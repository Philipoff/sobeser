import SobeserLogo from './SobeserLogo.vue'

export default {
  title: 'SobeserLogo',
  component: SobeserLogo,
  tags: ['autodocs'],
}

export const Default = () => ({
  components: { SobeserLogo },
  template: `<SobeserLogo start="#6B7AFE" end="#083CC6" />`,
})

export const White = () => ({
  components: { SobeserLogo },
  template: `<div class="bg-primary">
    <SobeserLogo start="#FFF"/>
  </div>`,
})

export const Blue = () => ({
  components: { SobeserLogo },
  template: `<SobeserLogo start="#0E41C9"/>`,
})

export const Height = () => ({
  components: { SobeserLogo },
  template: `<SobeserLogo start="#6B7AFE" end="#083CC6" :height="48"/>`,
})
